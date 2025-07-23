import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

def caption_image(img):
    img = img.convert("RGB")
    inputs = processor(images=img, return_tensors="pt").to(device)
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

with gr.Blocks() as demo:
    # Title and subtitle with centered styling
    gr.HTML("""
    <h1 style="text-align:center; font-size: 4rem; color: #007BFF; margin-bottom: 0; user-select:none;">
        ❄️ ICEY
    </h1>
    <p style="text-align:center; font-size: 1.4rem; color: #555; margin-top: 0;">
        Intelligent Captioning Engine for You
    </p>
    """)

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="Upload Image", type="pil")
            generate_btn = gr.Button("Generate Caption")
            clear_btn = gr.Button("Clear")
        with gr.Column():
            caption_output = gr.Textbox(label="Generated Caption", lines=4)
            feedback = gr.Radio(
                ["👍 Helpful", "👎 Needs Improvement"],
                label="Was this caption helpful?"
            )

    generate_btn.click(fn=caption_image, inputs=image_input, outputs=caption_output)
    clear_btn.click(fn=lambda: (None, ""), inputs=[], outputs=[image_input, caption_output])

    # Footer text
    gr.HTML("""
    <p style="text-align:center; font-style: italic; color: gray; margin-top: 50px;">
        This project uses <a href="https://huggingface.co/Salesforce/blip-image-captioning-base" target="_blank">Salesforce BLIP</a> image captioning model.
    </p>
    """)

demo.launch()
