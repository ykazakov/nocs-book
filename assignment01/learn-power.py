import ipywidgets as widgets
slider = widgets.IntSlider(min=0,max=10,readout=False,)
text = widgets.HTML()
def display_value(v):
    text.value = f'<big>2<sup>{v}</sup> = <b>{2**v}</b></big>'
display_value(slider.value)
def value_changed(change):
    display_value(slider.value)
slider.observe(value_changed, 'value')    

layout = widgets.HBox([slider, text])
display(layout)