# SOPHIA NEAD

> Linha adicional de texto informativo sobre o que o projeto faz. Sua introdução deve ter cerca de 2 ou 3 linhas. Não exagere, as pessoas não vão ler.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [x] CRUD entidade polo
- [ ] Tarefa 2
- [ ] Tarefa 3
- [ ] Tarefa 4
- [ ] Tarefa 5

## 💻 Pré-requisitos

- Python `version 10`

## Entidades

| Nome | Att1 | Att2 | Att3 | Att4 | Att5 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| Polo | id   | nome | -    | -    | -    |
| -    | -    | -    | -    | -    | -    |


## Entidade Polo
### CREATE POLO
```python
from src.controllers.polo_controller import PoloController
from src.schemas.polo_schema import PoloInput

polo = PoloInput(nome='Itaperuna')
polo_controller.create_polo(polo)
```

### FIND ALL POLO
```python
from src.controllers.polo_controller import PoloController

polos = polo_controller.find_all_polo()
```

### FIND BY ID POLO
```python
from src.controllers.polo_controller import PoloController

polo_controller.find_by_id_polo(<id>)
```

### UPDATE POLO
```python
from src.controllers.polo_controller import PoloController

novoPolo = PoloInput(<id>, <novo_nome>)
polo_controller.update_polo(novoPolo)
```

### DELETE POLO
```python
from src.controllers.polo_controller import PoloController

polo_controller.delete_polo(<id>)
```


## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
