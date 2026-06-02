# from functools import wraps
# from src.models.entitys_model import EntitysModel
# from datetime import date


# def UpsertDecorator(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         dto: EntitysModel = args[1]

#         service: ServiceInterface = args[0]

#         data_atual = date.today()

#         entity_all = service.find_all()

#         for entity in entity_all:

#             same_entity = (
#                 dto.entity_name == entity.entity_name
#                 and dto.unidade == entity.unidade
#                 and dto.sistema == entity.sistema
#                 and data_atual == entity.data
#             )

#             if not same_entity:
#                 continue

#             entity.oldExternalId = dto.oldExternalId
#             entity.newExternalId = dto.newExternalId

#             return service.update(entity)

#         return func(*args, **kwargs)

#     return wrapper
