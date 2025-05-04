from multiprocessing import Manager

manager = Manager()
shared_data = manager.dict()