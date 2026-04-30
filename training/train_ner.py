import json
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    TrainingArguments,
    Trainer,
    DataCollatorForTokenClassification,
)

# -------------------------
# Load Data
# -------------------------

def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Dataset.from_list(data)


train_dataset = load_data("training/data/train.json")
val_dataset = load_data("training/data/validation.json")

# -------------------------
# Labels
# -------------------------

label_list = [
    "O",
    "B-NAME", "I-NAME",
    "B-LOCATION", "I-LOCATION",
    "B-DATE", "I-DATE",
    "B-PHONE", "I-PHONE",
    "B-EMAIL", "I-EMAIL",
    "B-HOSPITAL_ID", "I-HOSPITAL_ID",
]

label2id = {label: index for index, label in enumerate(label_list)}
id2label = {index: label for label, index in label2id.items()}


def encode_labels(example):
    example["labels"] = [label2id[tag] for tag in example["ner_tags"]]
    return example


train_dataset = train_dataset.map(encode_labels)
val_dataset = val_dataset.map(encode_labels)

# -------------------------
# Tokenizer
# -------------------------

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")


def tokenize_and_align_labels(example):
    tokenized = tokenizer(
        example["tokens"],
        truncation=True,
        is_split_into_words=True,
    )

    word_ids = tokenized.word_ids()
    aligned_labels = []
    previous_word_id = None

    for word_id in word_ids:
        if word_id is None:
            aligned_labels.append(-100)
        elif word_id != previous_word_id:
            aligned_labels.append(example["labels"][word_id])
        else:
            aligned_labels.append(-100)

        previous_word_id = word_id

    tokenized["labels"] = aligned_labels
    return tokenized


train_dataset = train_dataset.map(tokenize_and_align_labels)
val_dataset = val_dataset.map(tokenize_and_align_labels)

# Remove original columns so Trainer only sees model inputs
train_dataset = train_dataset.remove_columns(["tokens", "ner_tags"])
val_dataset = val_dataset.remove_columns(["tokens", "ner_tags"])

# This handles dynamic padding correctly
data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

# -------------------------
# Model
# -------------------------

model = AutoModelForTokenClassification.from_pretrained(
    "bert-base-cased",
    num_labels=len(label_list),
    id2label=id2label,
    label2id=label2id,
)

# -------------------------
# Training Args
# -------------------------

training_args = TrainingArguments(
    output_dir="training/saved_model",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=3,
    weight_decay=0.01,
    save_strategy="epoch",
    eval_strategy="epoch",
    logging_steps=1,
)

# -------------------------
# Trainer
# -------------------------

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=data_collator,
    processing_class=tokenizer,
)

# -------------------------
# Train + Save
# -------------------------

trainer.train()

trainer.save_model("training/saved_model")
tokenizer.save_pretrained("training/saved_model")

print("Model training completed and saved to training/saved_model")