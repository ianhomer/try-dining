public class Dining {
  public static void main(String[] args) {
    System.out.println("Hello");
    new Philosophers().eat();
  }

  static class Philosophers {
    void eat() {
      System.out.println("Eating");
    }
  }
}