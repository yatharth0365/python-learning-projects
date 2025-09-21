# Flash Card App 🎯

A French-English vocabulary learning application built with Python and Tkinter. Master new words with interactive flashcards that help you memorize vocabulary effectively!

## 📸 Preview

The app features a clean, intuitive interface with:
- Card front: French word
- Card back: English translation  
- Right/Wrong buttons for self-assessment
- Progress tracking

## ✨ Features

- **Interactive Flash Cards**: Click to flip between French and English
- **Self-Assessment**: Mark words as known or unknown
- **Progress Tracking**: Cards you know are removed from the deck
- **Data Persistence**: Your progress is saved automatically
- **Clean GUI**: Simple, distraction-free interface

## 🚀 How to Run

1. **Prerequisites**: Make sure you have Python 3.x installed
2. **Install Dependencies**:
   ```bash
   pip install pandas tkinter
   ```
   Note: Tkinter usually comes pre-installed with Python

3. **Run the Application**:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
flash-card-app/
├── main.py              # Main application file
├── data/
│   └── french_words.csv # Vocabulary data (French-English pairs)
├── images/
│   ├── card_front.png   # Front card background
│   ├── card_back.png    # Back card background
│   ├── right.png        # Right button icon
│   └── wrong.png        # Wrong button icon
└── README.md            # This file
```

## 🎮 How to Use

1. **Start the app**: Run `python main.py`
2. **Study mode**: 
   - A French word appears on the card
   - Try to remember the English translation
   - Click the card or wait 3 seconds to see the answer
3. **Self-assess**:
   - Click ✅ (Right) if you knew the word
   - Click ❌ (Wrong) if you didn't know it
4. **Progress**: Words you mark as "right" are removed from your study deck

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework for the interface
- **Pandas** - Data manipulation and CSV handling
- **CSV** - Data storage format for vocabulary

## 💡 Learning Concepts

This project demonstrates:
- GUI development with Tkinter
- File I/O operations
- Data manipulation with Pandas
- Event-driven programming
- Timer functions and threading

## 🔮 Future Enhancements

- [ ] Add multiple language pairs
- [ ] Implement spaced repetition algorithm  
- [ ] Add statistics and progress visualization
- [ ] Support for custom vocabulary lists
- [ ] Audio pronunciation feature

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

⭐ **Enjoyed this project?** Give it a star and check out my other Python learning projects!