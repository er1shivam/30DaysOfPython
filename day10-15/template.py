import os

def get_template_path(path):
    file_path = os.path.join(os.getcwd(),path)
    if not os.path.isfile(file_path):
        raise Exception("file not found")
    return file_path

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

def render_msg(template_str,context):
    return template_str.format(**context)

file_ = "template\email_message.txt"
template = get_template(file_)
file_html = "template\email_message.html"
template_html = get_template(file_html)
context = {
    "name": "Shivam",
    "date": None,
    "total": None
}

print(render_msg(template,context))
print(render_msg(template_html,context))