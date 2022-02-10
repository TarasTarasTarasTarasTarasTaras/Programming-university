from Observer import Observer

class Event:
    @staticmethod
    def update(key, observer, old_list, list_of_values, pos_or_range, new_list):
        for listener in observer.get_listeners():
            if key == listener:
                observer.get_listeners()[listener](old_list, list_of_values, pos_or_range, new_list)
                return
