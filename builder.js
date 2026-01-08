class Address {
  constructor(street, city, state, zip) {
    this.street = street;
    this.city = city;
    this.state = state;
    this.zip = zip;
  }
}

class User {
  constructor(name) {
    this.name = name;
  }
}
class UserBuilder {
  constructor(name) {
    this.user = new User(name);
  }

  setAge(age) {
    this.user.age = age;
    return this;
  }
  setPhone(phone) {
    this.user.phone = phone;
    return this;
  }
  setAddress(address) {
    this.user.address = address;
    return this;
  }
  build() {
    return this.user;
  }
}

let user = new UserBuilder("John Doe")
  .setAge(30)
  .setPhone("123-456-7890")
  .setAddress(new Address("123 Main St", "Anytown", "CA", "12345"))
  .build();
console.log(user);
