from IPython.core.magic import register_line_cell_magic
from IPython.display import display, Markdown

@register_line_cell_magic
def prompt_chatgpt(line:str, cell:str, model="gpt-3.5-turbo"):
    """A prompt helper function that sends a message to openAI
    and prints out the text response.
    """
    from openai import OpenAI
    
    message = line + "\n" + cell
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}]
    )
    text = response.choices[0].message.content
    display(Markdown(text))
    