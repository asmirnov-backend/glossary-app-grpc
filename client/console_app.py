import grpc
from generated import glossary_pb2, glossary_pb2_grpc
import logging

def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = glossary_pb2_grpc.GlossaryServiceStub(channel)
        
        try:
            while True:
                print("\n=== Меню операций ===")
                print("1. Создать термин")
                print("2. Поиск терминов по имени")
                print("3. Список терминов")
                print("4. Получить термин")
                print("5. Обновить термин")
                print("6. Удалить термин")
                print("7. Выйти")
                
                choice = input("Выберите операцию (1-7): ")
                
                if choice == "1":
                    print("\n=== Создание термина ===")
                    term_name = input("Введите название термина: ")
                    term_description = input("Введите описание термина: ")
                    term = stub.CreateTerm(glossary_pb2.CreateTermRequest(
                        term=term_name,
                        description=term_description
                    ))
                    print(f"Создан термин: {term.term} - {term.description}")
                
                elif choice == "2":
                    print("\n=== Поиск терминов по имени ===")
                    query = input("Введите поисковый запрос: ")
                    search_request = glossary_pb2.SearchTermsRequest(query=query)
                    for term in stub.SearchTerms(search_request):
                        print(f"Найдено: {term.term} - {term.description}")
                
                elif choice == "3":
                    print("\n=== Список терминов ===")
                    skip = int(input("Введите количество терминов для пропуска: "))
                    limit = int(input("Введите лимит терминов: "))
                    response = stub.ListTerms(glossary_pb2.ListTermsRequest(
                        skip=skip,
                        limit=limit
                    ))
                    print(f"Всего терминов: {response.total}")
                    for term in response.terms:
                        print(f"- {term.term}: {term.description}")
                
                elif choice == "4":
                    print("\n=== Получение термина ===")
                    term_name = input("Введите название термина: ")
                    term = stub.GetTerm(glossary_pb2.GetTermRequest(term=term_name))
                    print(f"Найден термин: {term.term} - {term.description}")
                
                elif choice == "5":
                    print("\n=== Обновление термина ===")
                    term_name = input("Введите название термина для обновления: ")
                    term_description = input("Введите новое описание термина: ")
                    updated_term = stub.UpdateTerm(glossary_pb2.UpdateTermRequest(
                        term=term_name,
                        description=term_description
                    ))
                    print(f"Обновлен термин: {updated_term.term} - {updated_term.description}")
                
                elif choice == "6":
                    print("\n=== Удаление термина ===")
                    term_name = input("Введите название термина для удаления: ")
                    delete_response = stub.DeleteTerm(glossary_pb2.DeleteTermRequest(term=term_name))
                    print(f"Результат удаления: {delete_response.message}")
                
                elif choice == "7":
                    print("Выход из программы.")
                    break
                
                else:
                    print("Неверный выбор. Пожалуйста, выберите операцию от 1 до 7.")

        except grpc.RpcError as e:
            print(f"Ошибка RPC: {e.details()}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()