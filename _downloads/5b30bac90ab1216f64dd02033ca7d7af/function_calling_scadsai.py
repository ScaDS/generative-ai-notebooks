def function_to_dict(func):
    """
    Takes a function definition and turns it into a dictionary, which later can be stored as json.
    
    The function should have a docstring explaining what the function can be used for and the parameters should have type definitions.
    """
    import inspect
    
    # Extracting function details
    func_name = func.__name__
    func_doc = func.__doc__.strip() if func.__doc__ else ""
    sig = inspect.signature(func)
    
    # Parsing parameters
    params = {
        "type": "object",
        "properties": {},
        "required": []
    }
    
    for name, param in sig.parameters.items():
        param_type = str(param.annotation) if param.annotation != inspect._empty else "unknown"
        
        if param_type == "<class 'str'>":
            param_type = "string" 
        elif param_type == "<class 'int'>":
            param_type = "integer" 
        elif param_type == "<class 'float'>":
            param_type = "number" 
        elif param_type == "<class 'bool'>":
            param_type = "boolean" 
        else:
            param_type = str(param_type).lower()
        
        params["properties"][name] = {
            "type": param_type
        }
        if param.default == inspect._empty:
            params["required"].append(name)
    
    # Constructing the dictionary structure
    func_dict = {
        "type": "function",
        "function": {
            "name": func_name,
            "description": func_doc,
            "parameters": params
        }
    }
    
    return func_dict


def call_function_from_response(tool_calls, named_tools, verbose=False):
    """
    Takes a response-string from ollama/mistral raw mode, extracts a function to be called and its parameters and calls the function.
    The function must be in the dictionary named_tools where keys are names of functions and values are the corresponding functions.
    """
    import json

    if len(tool_calls) == 0:
        raise ValueError("Not a function call")

    for tool_call in tool_calls:
        func = tool_call.function
        func_name = func.name
        arguments = json.loads(func.arguments)

        result = named_tools[func_name](**arguments)
        return result

        # Todo: What if multiple functions should be called?
    

def prompt_scadsai_llm(message, tool_dicts, endpoint:str= "https://llm.scads.ai/v1", model:str="meta-llama/Llama-3.3-70B-Instruct", verbose=False):
    """
    Submit a prompt to a remotely running model and returns the response.
    """
    import os
    
    # format the list of function tools to be a single line
    #message = message.replace("\n", " ")
    #while "  " in message:
    #    message = message.replace("  ", " ")

    api_key = os.environ.get('SCADSAI_API_KEY')
    
    import openai
    client = openai.OpenAI(base_url=endpoint,
                       api_key=api_key)

    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        tools=tool_dicts,
    )
    
    return completion

    
def act(prompt:str, tools:list):
    """
    Takes a prompt and a list of function tools, and turns it into a prompt to a function-calling capable language model.
    If the model can select a function to call considering the prompt, this function will be called.
    """
    # get a dictionary with names of functions as keys, and corresponding functions as values
    named_tools = {f.__name__: f for f in tools}
    
    # convert the functions to json
    tool_dicts = [function_to_dict(f) for f in tools] 
        
    # submit the prompt
    completion = prompt_scadsai_llm(prompt, tool_dicts)
    
    # call the function as specified in the response
    return call_function_from_response(completion.choices[0].message.tool_calls, named_tools)