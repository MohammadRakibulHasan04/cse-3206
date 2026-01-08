class Prototype {
  clone() {
    throw new Error("Clone method must be implemented");
  }
}

class ConcretePrototype extends Prototype {
  constructor(name, value) {
    super();
    this.name = name;
    this.value = value;
  }

  clone() {
    return new ConcretePrototype(this.name, this.value);
  }

  display() {
    console.log(`Name: ${this.name}, Value: ${this.value}`);
  }
}

const original = new ConcretePrototype("Original", 100);
console.log("Original Object:");
original.display();

const clone1 = original.clone();
clone1.name = "Clone 1";
clone1.value = 200;

const clone2 = original.clone();
clone2.name = "Clone 2";
clone2.value = 300;

console.log("\nCloned Objects:");
clone1.display();
clone2.display();

console.log("\nOriginal Object (unchanged):");
original.display();
