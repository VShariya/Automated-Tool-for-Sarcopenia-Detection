import gradio as gr
from Sarcopenia_Test import run_pipeline, list_weights

with gr.Blocks(title="Sarcopenia Analysis", theme=gr.themes.Soft()) as demo:
    gr.Markdown("## Sarcopenia Detection UI")

    with gr.Row():
        # LEFT side → results
        with gr.Column(scale=2):
            gr.Markdown("### Results")
            metrics_df   = gr.Dataframe(label="Metrics", interactive=False, wrap=True)
            metrics_json = gr.JSON(label="Metrics (JSON)")
            csv_out      = gr.File(label="Download metrics.csv")
            json_out     = gr.File(label="Download sarcopenia_report.json")
            report_text  = gr.Textbox(label="Clinical Report", lines=10, interactive=False)
            status       = gr.Textbox(label="Status / Log", interactive=False)

        # RIGHT side → inputs
        with gr.Column(scale=1):
            in_file = gr.File(label="Upload NIfTI file", file_types=["file"], type="filepath")
            model_dd = gr.Dropdown(label="Choose model weights", choices=list_weights(), value=None)
            refresh = gr.Button("Refresh Model List")
            device_sel = gr.Radio(label="Device", choices=["auto", "cpu", "cuda"], value="auto")
            ts_cpu = gr.Checkbox(label="Force TotalSegmentator on CPU", value=False)

            # Patient info
            height_cm = gr.Number(label="Patient Height (cm)", value=170)
            gender = gr.Radio(label="Sex", choices=["male", "female"], value="female")

            run_btn = gr.Button("Run pipeline", variant="primary")

    # Auto populate model dropdown from weights/
    refresh.click(fn=list_weights, outputs=model_dd)
    demo.load(fn=list_weights, outputs=model_dd)

    # Button wiring
    run_btn.click(
        fn=run_pipeline,
        inputs=[in_file, model_dd, device_sel, ts_cpu, height_cm, gender],
        outputs=[
            metrics_df, metrics_json, csv_out, json_out, report_text, status
        ]
    )

if __name__ == "__main__":
    demo.queue().launch(share=True)
