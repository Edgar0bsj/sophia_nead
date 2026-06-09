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
<!-- ================================================================================== -->

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
{
    'id': 1,
    'data': datetime.date(2026, 6, 8),
    'sistema': 'SOPHIA',
    'unidade': 'NOVA IGUAÇU',
    'entity_name': 'campus',
    'oldExternalId': '987654321',
    'newExternalId': '123456789'
}
```

</details>
<!-- ================================================================================== -->

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
<!-- ================================================================================== -->

#### update_entity

<hr>

```python
  update_entity(id, entity_inputDTO)
```

<details>
  <summary> Parameters </summary>

| Parameter         | Type             | Description                                |
| :---------------- | :--------------- | :----------------------------------------- |
| `id`              | `int`            | -                                          |
| `entity_inputDTO` | `EntityInputDTO` | **Required**, Pacote->`src.dto.entityDTO`. |

</details>

<details>
  <summary> Exemplo de uso </summary>

```python
    registros = controller.find_all_entity()
    ultimo_registro = registros[-1]

    entity = EntityInputDTO(
        ultimo_registro["sistema"],
        ultimo_registro["unidade"],
        "novoRegistro",
        ultimo_registro["oldExternalId"],
        ultimo_registro["newExternalId"]
    )

    controller.update_entity(
        ultimo_registro["id"],
        entity
    )
```

</details>

<details>
  <summary> Retorna esperado </summary>

```python
{
    'id': 1,
    'data': datetime.date(2026, 6, 8),
    'sistema': 'SOPHIA',
    'unidade': 'NOVA IGUAÇU',
    'entity_name': 'novoRegistro',
    'oldExternalId': '987654321',
    'newExternalId': '123456789'
}
```

</details>
<!-- ================================================================================== -->

#### delete_entity

<hr>

```python
  delete_entity(id)
```

<details>
  <summary> Parameters </summary>

| Parameter | Type  | Description |
| :-------- | :---- | :---------- |
| `id`      | `int` | -           |

</details>

<details>
  <summary> Exemplo de uso </summary>

```python
entity = controller.find_all_entity()[-1]

controller.delete_entity(entity["id"])
```

</details>

<details>
  <summary> Retorna esperado </summary>

```python
None
```

</details>

<!-- ================================================================================== -->

#### export_entity_to_CSV

<hr>

```python
  export_entity_to_CSV()
```

<details>
  <summary> Parameters </summary>

| Parameter | Type   | Description |
| :-------- | :----- | :---------- |
| `None`    | `None` | `-`         |

</details>

<details>
  <summary> Exemplo de uso </summary>

```python
controller.export_entity_to_CSV()
```

</details>

<details>
  <summary> Retorna esperado </summary>

```python
None
```

</details>
