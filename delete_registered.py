import pickle

target_id = input("Enter Registration ID to delete: ").strip()

with open("face_db.pkl", "rb") as f:
    encodings, names, ids = pickle.load(f)

new_encodings = []
new_names = []
new_ids = []

removed = 0

for enc, name, reg_id in zip(encodings, names, ids):
    if reg_id != target_id:
        new_encodings.append(enc)
        new_names.append(name)
        new_ids.append(reg_id)
    else:
        removed += 1

if removed == 0:
    print("No such Registration ID found.")
else:
    with open("face_db.pkl", "wb") as f:
        pickle.dump((new_encodings, new_names, new_ids), f)
    print(f"Deleted {removed} face samples for RegID {target_id}")