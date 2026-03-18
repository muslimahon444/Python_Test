import unittest
def add_task(tasks,new_task):
    if not new_task.strip() :
        return False
    tasks.append(new_task)
    return True
class TestSmartmanager(unittest.TestCase):
    def test_add_task_success(self):
        tasks = []
        result = add_task(tasks,'Завершить лабараторную')
        self.assertTrue(result)
        self.assertEqual(len(tasks),1)
        
    def test_add(self):
        tasks =[]
        result = add_task(tasks,' ')
        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()
    
