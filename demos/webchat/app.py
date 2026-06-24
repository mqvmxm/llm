import web
from ollama import chat

urls = (
    '/', 'Index',
)

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    
    def ia(self, prompt):
        response = chat(
            model='llama3.2:3b',
            messages=[
                {
                    'role': 'user', 
                    'content': prompt
                }
            ],
        )
        return response.message.content

    def GET(self):
        pregunta = ""
        respuesta = ""
        return render.index(pregunta, respuesta)

    def POST(self):
        formulario = web.input()
        prompt = formulario['prompt']
        respuesta = self.ia(prompt)
        return render.index(prompt, respuesta)

if __name__ == "__main__":
    app.run()