def enroll_student():
    name = simpledialog.askstring("Enroll", "Enter Name")
    if not name:
        return

    reg_id = simpledialog.askstring("Enroll", "Enter Registration ID")
    if not reg_id:
        return

    db = load_db()

    # Duplicate protection
    if reg_id in db:
        overwrite = messagebox.askyesno(
            "Already Exists",
            "This Registration ID already exists.\nDo you want to re-enroll and overwrite?"
        )
        if not overwrite:
            return

    cap = cv2.VideoCapture(0)
    collected_encodings = []
    REQUIRED = 20

    while len(collected_encodings) < REQUIRED:
        ret, frame = cap.read()
        if not ret:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb)

        if len(locations) == 1:
            encoding = face_recognition.face_encodings(rgb, locations)[0]
            collected_encodings.append(encoding)

            top, right, bottom, left = locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"Samples: {len(collected_encodings)}/{REQUIRED}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Enrollment (Press Q to cancel)", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            return

    cap.release()
    cv2.destroyAllWindows()

    # 🔴 CORE CHANGE: average encoding
    avg_encoding = sum(collected_encodings) / len(collected_encodings)

    db[reg_id] = {
        "name": name,
        "encoding": avg_encoding,
        "samples": REQUIRED,
        "enrolled_on": datetime.now().strftime("%Y-%m-%d")
    }

    save_db(db)
    messagebox.showinfo("Success", f"{name} enrolled successfully")
