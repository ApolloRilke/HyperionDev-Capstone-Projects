public class Person {

	// Attributes of Person 
	String type;		// Architect, contractor, or customer, etc
	String name;		
	String telephoneNo;
	String email;
	String address;		// Physical address of person

	//Person constructor
	public Person(String type, String name, String telephoneNo, String email, String address) {
		this.type = type;
		this.name = name;
		this.telephoneNo = telephoneNo;
		this.email = email;
		this.address = address;
	}

	public String toString() {
		String output = type + "'s information: \nName: " + name;
		output += "\nTelephone number: " + telephoneNo;
		output += "\nEmail address: " + email;
		output += "\nAddress: " + address;
		
		return output;
	}
}