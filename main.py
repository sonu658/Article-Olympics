import gradio as gr
import re

def remove_articles(text):
    articles = [' a ', ' an ', ' the ']
    for article in articles:
        text = text.replace(article, ' ')
    return re.sub(' +', ' ', text).strip()

def fix_sentences(wrong_sents):
    lines = wrong_sents.strip().split('\n')
    output = "✍️ Rewrite each sentence with the correct articles:\n\n"
    for i, line in enumerate(lines):
        output += f"{i+1}. {line}\n"
    return output

def discuss_articles():
    return (
        "📚 **Why Articles Matter:**\n\n"
        "- **'A' / 'An'** are used for non-specific or first-time references.\n"
        "- **'The'** is used when referring to something specific or already known.\n"
        "- Articles help make your message clear and precise.\n"
        "- Example: *A cat sat on the mat.* (Not just any mat — a specific one!)"
    )

def describe_object(object_name, description):
    return f"📝 **Description of {object_name}:**\n\n{description}"

with gr.Blocks(title="Article Olympics 🏆") as demo:
    gr.Markdown(
        "<h1 style='color:#4ecdc4;'>🏆 Article Olympics</h1>"
        "<p>Learn and practice using <strong>'a', 'an',</strong> and <strong>'the'</strong> in fun ways!</p>"
    )

    with gr.Tab("1️⃣ Remove Articles"):
        gr.Markdown("### 🧹 Remove All Articles from a Paragraph")
        article_input = gr.Textbox(lines=5, label="Enter a Paragraph")
        article_output = gr.Textbox(label="Without Articles", interactive=False)
        remove_btn = gr.Button("🗑️ Remove Articles")
        remove_btn.click(remove_articles, inputs=article_input, outputs=article_output)

    with gr.Tab("2️⃣ Fix Incorrect Sentences"):
        gr.Markdown("### 🛠️ Fix Sentences with Wrong Article Usage")
        wrong_sentences = gr.Textbox(lines=6, label="Paste 5 Sentences with Mistakes")
        fix_output = gr.Textbox(lines=7, label="Correct Them Below")
        fix_btn = gr.Button("✅ Show Sentences to Correct")
        fix_btn.click(fix_sentences, inputs=wrong_sentences, outputs=fix_output)

    with gr.Tab("3️⃣ Why Articles Matter"):
        gr.Markdown("### 📖 Learn Why Articles Are Important")
        article_info = gr.Textbox(lines=10, label="Explanation", interactive=False)
        explain_btn = gr.Button("📘 Explain Articles")
        explain_btn.click(discuss_articles, outputs=article_info)

    with gr.Tab("4️⃣ Describe an Object"):
        gr.Markdown("### 📝 Describe an Object Using Proper Articles")
        obj_name = gr.Textbox(label="Object Name (e.g., pen, bag)")
        obj_desc = gr.Textbox(lines=4, label="Description Using Articles")
        obj_output = gr.Textbox(label="Formatted Output", interactive=False)
        desc_btn = gr.Button("📄 Generate Description")
        desc_btn.click(describe_object, inputs=[obj_name, obj_desc], outputs=obj_output)

demo.launch()
