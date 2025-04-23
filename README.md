# Perdocumen 1.1
### Usage
В папку _/input_ кладем код.

Выполняем:
```
docker build -t perdocumen:1.1 .
docker run -v $(pwd)/input:/opt/codebase -v $(pwd)/output:/opt/tutorial -e "DEEPSEEK_API_KEY=<your-api-key>" perdocumen:1.1
```
Забираем документацию в _/output_.

### Known issues
Если появляется ошибка _"This model's maximum context length is 65536 tokens. However, you requested 82942 tokens (82942 in the messages, 0 in the completion). Please reduce the length of the messages or completion."_ - нужно уменьшить количество/объем файлов репозитория. К сожалению, API Deepseek ограничено 65к токенов в контексте.

### Credits
Докер имплементация https://github.com/The-Pocket/Tutorial-Codebase-Knowledge
