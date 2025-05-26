📧 Envio de E-mails com HTML — Python

Este script foi criado com o objetivo de facilitar o envio de e-mails personalizados com conteúdo em HTML, ideal para apresentações profissionais como o envio de currículos, convites ou newsletters.

Ele lê um arquivo .html, monta a estrutura do e-mail e o envia automaticamente utilizando o servidor SMTP do Gmail. É uma solução simples e eficaz para quem precisa disparar e-mails com uma aparência mais moderna e profissional.
✨ Por que usar este script?

    Permite enviar e-mails com visual profissional (HTML).

    Facilita a automação do envio de currículos.

    Evita copiar e colar o conteúdo toda vez — basta editar o HTML.

    É leve, direto e usa bibliotecas padrão do Python.

⚙️ Como funciona?

    O HTML é armazenado em uma pasta separada (Emails_html/emailCurriculo.html).

    As credenciais do e-mail (usuário e senha de app) são lidas a partir de um arquivo .env, mantendo a segurança e a organização.

    O script configura a conexão com o servidor SMTP do Gmail, anexa o conteúdo HTML ao corpo do e-mail e envia a mensagem.