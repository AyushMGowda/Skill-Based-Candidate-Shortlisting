import tkinter as tk
from tkinter import messagebox, simpledialog

class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

def calculate_score(required_skills, candidate):
    return sum(1 for skill in candidate.skills if skill in required_skills)

def evaluate():
    required_skills = required_entry.get().strip().split()
    if not required_skills:
        messagebox.showwarning("Error", "Please enter required skills.")
        return

    if not candidates:
        messagebox.showwarning("Error", "No candidates added yet.")
        return

    ranking = [(c.name, calculate_score(required_skills, c)) for c in candidates]
    ranking.sort(key=lambda x: x[1], reverse=True)

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "=== Candidate Ranking ===\n\n")
    for name, score in ranking:
        result_box.insert(tk.END, f"{name} -> {score} matched skills\n")
    result_box.insert(tk.END, f"\nTop Candidate: {ranking[0][0]}")

def add_candidate():
    name = name_entry.get().strip()
    skills = skills_entry.get().strip().split()

    if not name or not skills:
        messagebox.showwarning("Error", "Enter both name and skills.")
        return

    candidates.append(Candidate(name, skills))
    messagebox.showinfo("Success", f"Added {name} successfully!")
    name_entry.delete(0, tk.END)
    skills_entry.delete(0, tk.END)

# --- UI Setup ---
root = tk.Tk()
root.title("Candidate Skill Matcher")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Candidate Name:").pack(pady=5)
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Candidate Skills (space separated):").pack(pady=5)
skills_entry = tk.Entry(root, width=50)
skills_entry.pack()

tk.Button(root, text="Add Candidate", bg="#4CAF50", fg="white", command=add_candidate).pack(pady=10)

tk.Label(root, text="Required Job Skills (space separated):").pack(pady=5)
required_entry = tk.Entry(root, width=50)
required_entry.pack()

tk.Button(root, text="Evaluate Candidates", bg="#2196F3", fg="white", command=evaluate).pack(pady=10)

result_box = tk.Text(root, height=10, width=60)
result_box.pack(pady=10)

candidates = []

root.mainloop()
