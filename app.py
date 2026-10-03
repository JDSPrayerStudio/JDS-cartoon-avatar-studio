import os
import asyncio
import gradio as gr
import edge_tts

async def generate_voiceover(text, voice_profile):
    voice_mapping = {
        "Andrew (Deep Gritty US Male)": "en-US-AndrewNeural",
        "Aria (Confident Cinematic Female)": "en-US-AriaNeural",
        "Christopher (Authoritative US Male)": "en-US-ChristopherNeural",
        "Guy (Smooth Street Motivation Male)": "en-US-GuyNeural"
    }
    selected_voice_id = voice_mapping.get(voice_profile, "en-US-AndrewNeural")
    output_audio = "avatar_voice.mp3"
    
    comm = edge_tts.Communicate(text, selected_voice_id, rate="+2%", pitch="-1Hz")
    await comm.save(output_audio)
    return output_audio

def process_avatar_video(image, text, voice_profile):
    if image is None:
        return "Please upload an avatar image first!", None
    if not text.strip():
        return "Please type a script for your avatar to speak!", None
        
    # Generate the voice audio from text
    audio_path = asyncio.run(generate_voiceover(text, voice_profile))
    
    # Placeholder for the AI animation processing hook 
    # (Here you plug in your LivePortrait or SadTalker inference function)
    status_message = "Avatar audio generated successfully! Ready to render animation."
    
    return status_message, audio_path

# Build the Web User Interface for Mobile & Desktop
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎨 Cartoon Avatar Motion Studio")
    gr.Markdown("Upload your cartoon character, type your motivational script, and bring your avatar to life.")
    
    with gr.Row():
        with gr.Column():
            avatar_image = gr.Image(type="filepath", label="Upload Avatar Image (PNG/JPG)")
            voice_choice = gr.Dropdown(
                choices=[
                    "Andrew (Deep Gritty US Male)",
                    "Aria (Confident Cinematic Female)",
                    "Christopher (Authoritative US Male)",
                    "Guy (Smooth Street Motivation Male)"
                ],
                value="Andrew (Deep Gritty US Male)",
                label="Select AI Voice"
            )
            script_input = gr.Textbox(
                lines=4, 
                placeholder="Type what you want your cartoon avatar to say...", 
                label="Avatar Speech Script"
            )
            generate_btn = gr.Button("Bring Avatar to Life 🚀", variant="primary")
            
        with gr.Column():
            output_status = gr.Textbox(label="Studio Status")
            output_audio = gr.Audio(label="Generated Voice Track", type="filepath")

    generate_btn.click(
        fn=process_avatar_video,
        inputs=[avatar_image, script_input, voice_choice],
        outputs=[output_status, output_audio]
    )

if __name__ == "__main__":
    demo.launch()
  
