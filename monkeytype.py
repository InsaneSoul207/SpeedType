import tkinter as tk
import random
import time

sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Typing practice helps improve your speed.",
    "Developing applications can be fun and rewarding.",
    "Always keep learning and improving your skills.",
    "Artificial intelligence is transforming industries.",
    "Data science combines statistics and programming.",
    "Machine learning algorithms can learn from data.",
    "The future of technology is exciting and unpredictable.",
    "Collaboration is key to successful project management.",
    "Effective communication enhances teamwork and productivity.",
    "Sustainable practices are essential for environmental health.",
    "Creativity and innovation drive progress in society.",
    "Problem-solving skills are vital in everyday life.",
    "Reading books expands your knowledge and perspective.",
    "Exercise is important for maintaining physical health.",
    "Mindfulness and meditation can reduce stress levels.",
    "Traveling exposes you to different cultures and ideas.",
    "Cooking at home can be both healthy and enjoyable.",
    "Music has the power to evoke emotions and memories.",
    "Learning a new language opens up opportunities.",
    "Financial literacy is crucial for personal success.",
    "Time management skills improve efficiency and focus.",
    "Networking can lead to new career opportunities.",
    "Volunteering benefits both the community and the individual.",
    "Technology is reshaping the way we live and work.",
    "Critical thinking is essential for informed decision-making.",
    "The internet has changed how we access information.",
    "Social media connects people across the globe.",
    "Online education provides flexibility and accessibility.",
    "Art and culture enrich our lives and communities.",
    "Science and technology continue to evolve rapidly.",
    "History teaches us valuable lessons about humanity.",
    "The importance of mental health awareness is growing.",
    "Healthy eating habits contribute to overall well-being.",
    "The impact of climate change is a pressing concern.",
    "Entrepreneurship fosters innovation and economic growth.",
    "Digital marketing is transforming business strategies.",
    "Research and development drive technological advancements.",
    "Public speaking skills can enhance your career prospects.",
    "The power of storytelling connects us as human beings.",
    "A good night's sleep is vital for health and productivity.",
    "Emotional intelligence plays a key role in relationships.",
    "The arts inspire creativity and self-expression.",
    "Understanding different perspectives promotes empathy.",
    "Setting goals helps to achieve personal and professional success.",
    "Life-long learning is essential in a changing world.",
    "Resilience is necessary to overcome challenges.",
    "The significance of cultural heritage should be preserved.",
    "Good leadership inspires and motivates teams.",
    "The role of women in leadership continues to grow.",
    "Cybersecurity is crucial in the digital age.",
    "The importance of clean water cannot be overstated.",
    "Public transportation systems are vital for urban mobility.",
]

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Practice App")
        self.root.geometry("600x500")
        self.root.configure(bg="#2E2E2E") 
        
        self.sample_text = random.choice(sample_texts)
        self.user_input = ""
        self.start_time = None
        self.end_time = None
        
        self.frame = tk.Frame(root, bg="#2E2E2E")
        self.frame.pack(pady=20)

        self.text_label = tk.Label(self.frame, text=self.sample_text, wraplength=500, font=("Arial", 14), bg="#2E2E2E", fg="white")
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(self.frame, font=("Arial", 14), width=40, bd=2, relief="groove", bg="#444444", fg="white")
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_typing)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), bg="#2E2E2E", fg="white")
        self.result_label.pack(pady=5)

        self.elapsed_time_label = tk.Label(root, text="Elapsed Time: 0.00 seconds", font=("Arial", 12), bg="#2E2E2E", fg="white")
        self.elapsed_time_label.pack(pady=5)

        self.speed_label = tk.Label(root, text="Speed: 0 WPM", font=("Arial", 12), bg="#2E2E2E", fg="white")
        self.speed_label.pack(pady=5)

        self.accuracy_label = tk.Label(root, text="Accuracy: 0%", font=("Arial", 12), bg="#2E2E2E", fg="white")
        self.accuracy_label.pack(pady=5)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart, font=("Arial", 12), bg="#4CAF50", fg="white", activebackground="#45a049")
        self.restart_button.pack(pady=(20, 40))  
        
    def check_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()  

        self.user_input = self.entry.get()

        elapsed_time = time.time() - self.start_time
        self.elapsed_time_label.config(text=f"Elapsed Time: {elapsed_time:.2f} seconds")

        correct_chars = sum(1 for a, b in zip(self.user_input, self.sample_text) if a == b)
        total_chars = len(self.user_input)  
        accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0

        self.accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")

        if event.keysym == "BackSpace":  
            accuracy -= 1  
            if accuracy < 0:
                accuracy = 0  

        if self.user_input == self.sample_text:
            self.end_time = time.time()
            self.calculate_speed(elapsed_time)
            self.result_label.config(text="Well done! You've completed the typing test.")
            self.entry.config(state="disabled")

    def calculate_speed(self, elapsed_time):
        words_typed = len(self.user_input.split())
        speed = (words_typed / elapsed_time) * 60 if elapsed_time > 0 else 0
        self.speed_label.config(text=f"Speed: {speed:.2f} WPM")

    def restart(self):
        self.user_input = ""
        self.start_time = None
        self.end_time = None
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.elapsed_time_label.config(text="Elapsed Time: 0.00 seconds")
        self.accuracy_label.config(text="Accuracy: 0%")
        self.speed_label.config(text="Speed: 0 WPM")
        self.sample_text = random.choice(sample_texts)
        self.text_label.config(text=self.sample_text) 

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()