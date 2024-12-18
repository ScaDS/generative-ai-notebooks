def print_messages(message_list):
    import autogen_core
    import json
    from IPython.display import Markdown, display
    for m in message_list:
        display(Markdown(f"**{m.source}:**\n\n"))
        #print(type(m), ":", m)
        if isinstance(m.content, str):
            display(Markdown(f"'{m.content}' \n\n"))
        else:
            for c in m.content:
                if isinstance(c, autogen_core._types.FunctionCall):
                    c_args = ", ".join([k + "=" + str(v) for k,v in json.loads(c.arguments).items()])
                    display(Markdown(f"{c.name}({c_args})\n\n"))
                elif isinstance(c, autogen_core.models._types.FunctionExecutionResult):
                    display(Markdown(f" = {c.content}\n\n"))    
                else:
                    display(Markdown(f"'{c}' \n\n"))