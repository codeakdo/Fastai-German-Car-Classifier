from fastai.vision.all import *
import gradio as gr

learn = load_learner('car_model_v2.pkl')

categories = ('Audi RS7', 'Mercedes G Wagon', 'Porsche 911')


def classify_image(img):
    pred, idx, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))


image = gr.Image(type="pil") 
label = gr.Label()

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label)
intf.launch(inline=False)