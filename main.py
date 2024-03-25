from time import sleep
from src.services.terminal_view_service import Item
from src.app import App


def main():
    app = App()
    
    app.encryptor_configuration_repository.init_db()
    app.secret_repository.init_db()
    app.secret_history_repository.init_db()
    
    app.authorization_service.create_if_not_exist()
    if not app.authorization_service.authorize():
        print("Not Authorized!")
        return
    
    app.view.add_menu_item(Item('Add Secret <Key> <Value>', 'create-secret', 'c', app.secret_use_case.create_secret))
    app.view.add_menu_item(Item('Get Secret', 'get-secret', 'g', app.secret_use_case.get_secret_by_key))
    app.view.add_menu_item(Item('Delete Secret', 'delete-secret', 'del', app.secret_use_case.delete_secret_by_key))
    app.view.add_menu_item(Item('Update Secret', 'update-secret', 'u', app.secret_use_case.update_secret_by_key))
    app.view.add_menu_item(Item('List Secrets', 'list-secrets', 'ls', app.secret_use_case.list_secrets))
    app.view.add_menu_item(Item('List Secret History', 'list-secret-history', 'lsh', app.secret_use_case.list_secret_history))
            
    app.view.run_main_loop()
    
    app.backup_service.create()
    app.backup_service.remove_old_backup()

main()
