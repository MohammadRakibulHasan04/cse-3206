interface Shape {
    double Area();
}

class Rectangle implements Shape {
    private double width;
    private double height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    public double Area() {
        return width * height;
    }
}

class Circle implements Shape {
    private double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    public double Area() {
        return Math.PI * radius * radius;
    }
}

class Ellipse implements Shape {
    private double R;
    private double r;
    
    public Ellipse(double R, double r) {
        this.R = R;
        this.r = r;
    }
    
    public double Area() {
        return R * r * Math.PI;
    }
}

// Abstract Creator
abstract class ShapeFactory {
    // Factory Method
    public abstract Shape createShape(double... params);
    
    // Template method that uses factory method
    public void displayArea() {
        Shape shape = createShape();
        System.out.println(getShapeName() + " Area: " + shape.Area());
    }
    
    protected String getShapeName() {
        return "Shape";
    }
}

// Concrete Creators
class RectangleFactory extends ShapeFactory {
    private double width;
    private double height;
    
    public RectangleFactory(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    public Shape createShape(double... params) {
        return new Rectangle(width, height);
    }
    
    @Override
    protected String getShapeName() {
        return "Rectangle";
    }
}

class CircleFactory extends ShapeFactory {
    private double radius;
    
    public CircleFactory(double radius) {
        this.radius = radius;
    }
    
    @Override
    public Shape createShape(double... params) {
        return new Circle(radius);
    }
    
    @Override
    protected String getShapeName() {
        return "Circle";
    }
}

class EllipseFactory extends ShapeFactory {
    private double R;
    private double r;
    
    public EllipseFactory(double R, double r) {
        this.R = R;
        this.r = r;
    }
    
    @Override
    public Shape createShape(double... params) {
        return new Ellipse(R, r);
    }
    
    @Override
    protected String getShapeName() {
        return "Ellipse";
    }
}

public class Main {
    public static void main(String[] args) {
        // Using Factory Method pattern
        ShapeFactory rectFactory = new RectangleFactory(5, 8);
        ShapeFactory circleFactory = new CircleFactory(7);
        ShapeFactory ellipseFactory = new EllipseFactory(4, 6);
        
        Shape rect = rectFactory.createShape();
        Shape circle = circleFactory.createShape();
        Shape ellipse = ellipseFactory.createShape();
        
        System.out.println("Rectangle Area: " + rect.Area());
        System.out.println("Circle Area: " + circle.Area());
        System.out.println("Ellipse Area: " + ellipse.Area());
        System.out.println("Total Area: " + (rect.Area() + circle.Area() + ellipse.Area()));
    }
}