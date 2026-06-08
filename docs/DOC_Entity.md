## API - Entity

#### Getting started

```python
  EntityController()
```

<details>
  <summary> Parameters </summary>

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
| `None`    | `-`  | -           |

</details>

<details>
  <summary> Exemplo de uso </summary>

```python
  controller = EntityController()
```

</details>

#### create_entity

<hr>

```python
  create_entity(EntityInputDTO)
```

<details>
  <summary> Parameters </summary>

| Parameter        | Type             | Description                                |
| :--------------- | :--------------- | :----------------------------------------- |
| `EntityInputDTO` | `EntityInputDTO` | **Required**, Pacote->`src.dto.entityDTO`. |

</details>

<details>
  <summary> Exemplo de uso </summary>

```python
entity_input = EntityInputDTO(
    sistema="SOPHIA",
    unidade="NOVA IGUAÇU",
    entity_name="campus",
    oldExternalId="987654321",
    newExternalId="123456789",
)

controller.create_entity(entity_input)
```

</details>

<details>
  <summary> Retorna esperado </summary>

```python
entity_input = EntityInputDTO(
    sistema="SOPHIA",
    unidade="NOVA IGUAÇU",
    entity_name="campus",
    oldExternalId="987654321",
    newExternalId="123456789",
)

controller.create_entity(entity_input)
```

</details>

#### find_all_entity

<hr>

```python
  find_all_entity()
```

<details>
  <summary> Parameters </summary>

| Parameter | Type | Description |
| :-------- | :--- | :---------- |
| `None`    | `-`  | -           |

</details>

<details>
  <summary> Exemplo de uso </summary>

```python
all_entitys = controller.find_all_entity()
```

</details>

<details>
  <summary> Retorna esperado </summary>

```python
[
    {
        'id': 1,
        'data': datetime.date(2026, 6, 8),
        'sistema': 'SOPHIA',
        'unidade': 'NOVA IGUAÇU',
        'entity_name': 'campus',
        'oldExternalId': '987654321',
        'newExternalId': '123456789'
    },
    ...
]
```

</details>
