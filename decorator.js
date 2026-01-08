class Component {
  operation() {
    return "Component";
  }
}

class ConcreteComponent extends Component {
  operation() {
    return "ConcreteComponent";
  }
}

class Decorator extends Component {
  constructor(component) {
    super();
    this.component = component;
  }

  operation() {
    return this.component.operation();
  }
}

class ConcreteDecoratorA extends Decorator {
  operation() {
    return `ConcreteDecoratorA(${super.operation()})`;
  }
}

class ConcreteDecoratorB extends Decorator {
  operation() {
    return `ConcreteDecoratorB(${super.operation()})`;
  }
}

const simple = new ConcreteComponent();
console.log("Simple component:", simple.operation());

const decoratorA = new ConcreteDecoratorA(simple);
console.log("Decorator A:", decoratorA.operation());

const decoratorB = new ConcreteDecoratorB(simple);
console.log("Decorator B:", decoratorB.operation());

const decoratorBoth = new ConcreteDecoratorB(new ConcreteDecoratorA(simple));
console.log("Both decorators:", decoratorBoth.operation());
