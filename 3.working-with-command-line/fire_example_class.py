import fire

class Calculator:
  def add(self, x, y):
    """Adds two numbers.""" 
    return x + y

  def subtract(self, x, y):
    """Subtracts two numbers."""
    return x - y

if __name__ == '__main__':
  fire.Fire(Calculator)