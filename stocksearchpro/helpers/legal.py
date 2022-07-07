import streamlit as st

def disclaimer(e=st) -> None:
    """Display the disclaimer in the app."""

    e.write("""<div class="custom-css-disclaimer">

> ###### Note: Please check the disclaimer and license before use. 
> 
> This is just a demonstration of machine learning, and not any financial advice.
> In a nutshell, your capital is at risk if you invest, even more so if you use our
> predictions. Please do not sue us.

</div>""", unsafe_allow_html=True)