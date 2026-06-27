import pickle

DB_FILE = "face_db.pkl"

with open(DB_FILE, "rb") as f:
    data = pickle.load(f)

print()

# ---------- NEW DICT-BASED DB ----------
if isinstance(data, dict):
    db = data
    print(f"Total registered students: {len(db)}\n")

    if not db:
        print("No students registered.")
    else:
        print("Registered students (sorted by Reg ID):\n")
        for reg_id in sorted(db.keys()):
            info = db[reg_id]
            print(
                f"Reg ID: {reg_id} | "
                f"Name: {info['name']} | "
                f"Samples: {info['samples']} | "
                f"Enrolled On: {info['enrolled_on']}"
            )

# ---------- OLD LIST-BASED DB ----------
elif isinstance(data, tuple) and len(data) == 3:
    encodings, names, ids = data

    unique_ids = sorted(set(ids))
    print(f"Total registered students: {len(unique_ids)}\n")
    print("Registered students (sorted by Reg ID):\n")

    for reg_id in unique_ids:
        name = names[ids.index(reg_id)]
        samples = ids.count(reg_id)
        print(
            f"Reg ID: {reg_id} | "
            f"Name: {name} | "
            f"Samples: {samples}"
        )

else:
    print("Unknown database format.")
