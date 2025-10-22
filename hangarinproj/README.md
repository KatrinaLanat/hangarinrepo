# Hangarin Dashboard Database Schema 🌸✨🌙

✨🌟 **Category** 🌟✨
- 🌸 <span style="color:#ffb6c1">id (PK) 🔑</span>
- 💖 <span style="color:#dda0dd">name ✨</span>

💫💖 **Priority** 💖💫
- 🌸 <span style="color:#ffb6c1">id (PK) 🔑</span>
- 💖 <span style="color:#dda0dd">name ✨🌟 **Category** 🌟✨
- 🌸 <span style="color:#ffb6c1">id (PK) 🔑</span>
- 💖 <span style="color:#dda0dd">name ✨</span>

💫💖 **Priority** 💖💫
- 🌸 <span style="color:#ffb6c1">id (PK) 🔑</span>
- 💖 <span style="color:#dda0dd">name ✨</span>

🌌🌙 **Task** 🌙🌌
- 🌸 <span style="color:#ffb6c1">id (PK) 🔑</span>
- 🌟 <span style="color:#87cefa">title 📝</span>
- 💖 <span style="color:#dda0dd">description ✏️</span>
- 🌙 <span style="color:#add8e6">due_date 📅</span>
- 💫 <span style="color:#ff69b4">category → Category.id 🎀</span>
- 💫 <span style="color:#ff69b4">priority → Priority.id 🌈</span>

🌙✨ **SubTask** ✨🌙
- 🌸 <span style="color:#ffb6c1">id (PK) 🔑</span>
- 🌟 <span style="color:#87cefa">title 📝</span>
- 💫 <span style="color:#ff69b4">task → Task.id 🌌</span>
- 🌿 <span style="color:#90ee90">is_done ✅</span>

📝🌟 **Note** 🌟📝
- 🌸 <span style="color:#ffb6c1">id (PK) 🔑</span>
- 💖 <span style="color:#dda0dd">content ✏️</span>
- 💫 <span style="color:#ff69b4">task → Task.id 🌌</span>
</span>
