import gradio as gr

# with gr.Blocks(css="Style.css") as demo:
with gr.Blocks() as demo:
    with gr.Tab(label='img2txt'):
        with gr.Row():
            with gr.Column(scale=15):
                txt1 = gr.Textbox(lines=2,label='')
                txt2 = gr.Textbox(lines=2,label='')
            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button(value='1')
                # button1 = gr.Button(value='1',elem_classes="btn")
                # button.click(fn,input,output)
                button2 = gr.Button(value='2')
                button3 = gr.Button(value='3')
                button4 = gr.Button(value='4')
            with gr.Column(scale=5):
                generate_button = gr.Button(value="Generate",variant='primary',scale=1)
                with gr.Row():
                    dropdown = gr.Dropdown(["1", "2", "3", "4"], label="Style1")
                    dropdown2 = gr.Dropdown(["1", "2", "3", "4"], label="Style2")
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    dropdown3 = gr.Dropdown(["A", "B", "C", "D"], label="Sampling method")
                    slider1 = gr.Slider(minimum=0, maximum=100, label="Sampling steps")
                checkboxgroup = gr.Checkboxgroup(["Restore faces", "Tiling", "Hires.fix"], label='')
                with gr.Row():
                    slider2 = gr.Slider(minimum=0, maximum=100, label="Width")
                    slider3 = gr.Slider(minimum=0, maximum=100, label="Batch count")
                with gr.Row():
                    slider4 = gr.Slider(minimum=0, maximum=100, label="Height")
                    slider5 = gr.Slider(minimum=0, maximum=100, label="Batch Size")
                slider6 = gr.Slider(minimum=0, maximum=100, label="CFG scale")
                with gr.Row():
                    number1 = gr.Number(label="Seed", scale=5)
                    button5 = gr.Button(value="Randomize", min_width=1)
                    button6 = gr.Button(value="Reset", min_width=1)
                    checkbox1 = gr.Checkbox(label="Extra")
                dropdown4 = gr.Dropdown(["A", "B", "C", "D"], label="Script")
            with gr.Column():
                with gr.Accordion():
                    gallery = gr.Gallery([
                        'https://dummyimage.com/300/09f.png',
                        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80',
                        "https://images.unsplash.com/photo-1554151228-14d9def656e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=386&q=80",
                        "https://images.unsplash.com/photo-1542909168-82c3e7fdca5c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aHVtYW4lMjBmYWNlfGVufDB8fDB8fA%3D%3D&w=1000&q=80",
                    ],columns=3)
                with gr.Row():
                    button6 = gr.Button(value="Save", min_width=1)
                    button7 = gr.Button(value="Save", min_width=1)
                    button8 = gr.Button(value="Zip", min_width=1)
                    button9 = gr.Button(value="Send to img2img", min_width=1)
                    button10 = gr.Button(value="Send to inpaint", min_width=1)
                    button11 = gr.Button(value="Send to extras", min_width=1)
                txt3 = gr.Textbox(lines=4, label="")
    with gr.Tab(label='txt'):
        pass
demo.launch()