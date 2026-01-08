class Target {
  request() {
    return "Target: Default behavior";
  }
}

class Adaptee {
  specificRequest() {
    return "Adaptee: Specific behavior";
  }
}

class Adapter extends Target {
  constructor(adaptee) {
    super();
    this.adaptee = adaptee;
  }

  request() {
    return `Adapter: ${this.adaptee.specificRequest()}`;
  }
}

function clientCode(target) {
  console.log(target.request());
}

console.log("Client: Working with Target:");
const target = new Target();
clientCode(target);

console.log("\nClient: Working with Adaptee via Adapter:");
const adaptee = new Adaptee();
const adapter = new Adapter(adaptee);
clientCode(adapter);
