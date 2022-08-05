import java.io.PrintStream;
import java.util.*;


public class Poised {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		System.out.println("Welcome to the project menu.");
		System.out.println("What would you like to do?");
		System.out.println("1 - enter a new project");
		System.out.println("2 - change the deadline of a project");
		System.out.println("3 - change the total amount of fee paid to date");
		System.out.println("4 - update a contractor's contact details");
		System.out.println("5 - finalise a project");
		System.out.println("6 - exit");

		int menu = scanner.nextInt();
		
		Project dummy = new Project(1, "Project Dummy", "House", "3 Staling Street", "RRF445", 5000, 2500, "04/09/2023");

		if (menu == 1) {
			System.out.println("Please enter the details of the project:");

			// Project details
			System.out.println("What is the project title?");			/////// If the user doesnt enter anything, then it must be under the name of the project
			String projectName = scanner.nextLine();
			System.out.println("What is the project number?");				////////////Do i assume its a special code? or is it just the sequential number?
			int projectNo = scanner.nextInt();
			System.out.println("What is the building type?");
			String buildingType = scanner.nextLine();
			System.out.println("What is the building address?");
			String projectAddress = scanner.nextLine();
			System.out.println("What is the project ERF number?");
			String erfNo = scanner.nextLine();
			System.out.println("The total cost of the project? \nR");  		/// check the R is in front of the number entered.
			double totalFee = scanner.nextDouble();
			System.out.println("How much has already been paid to date? \nR");  		/// Assuming its not 0...check the R is in front of the number entered.
			double feePaid = scanner.nextDouble();
			System.out.println("Enter the deadline: (dd/mm/yyyy)");  	////// Check the date entries or whatever..
			String deadline = scanner.nextLine();

			// Project details relating to the persons involved.
			// Architect 
			System.out.println("The following information will pertain to the architect assigned"
					+ " to this project.");
			System.out.println("Enter the name of the architect:");
			String architectName = scanner.nextLine(); 
			System.out.println("Enter their telephone number:");
			String architectTelephone = scanner.nextLine(); 
			System.out.println("Enter their email address:");
			String architectEmail = scanner.nextLine(); 
			System.out.println("Enter the name of the architect:");
			String architectAddress = scanner.nextLine(); 

			// Contractor
			System.out.println("The following information will pertain to the contractor assigned"
					+ " to this project.");
			System.out.println("Enter the name of the contractor:");
			String contractorName = scanner.nextLine(); 
			System.out.println("Enter their telephone number:");
			String contractorTelephone = scanner.nextLine(); 
			System.out.println("Enter their email address:");
			String contractorEmail = scanner.nextLine(); 
			System.out.println("Enter the name of the contractor:");
			String contractorAddress = scanner.nextLine(); 

			// Customer
			System.out.println("The following information will pertain to the customer assigned"
					+ " to this project.");
			System.out.println("Enter the name of the customer:");
			String customerName = scanner.nextLine(); 
			System.out.println("Enter their telephone number:");
			String customerTelephone = scanner.nextLine(); 
			System.out.println("Enter their email address:");
			String customerEmail = scanner.nextLine(); 
			System.out.println("Enter the name of the customer:");
			String customerAddress = scanner.nextLine(); 


			// Project name if left blank
			if (projectName == null) {
				projectName = buildingType + " " + architectName;
			}


			// Create a Project Object
			Project project = new Project(projectNo, projectName, buildingType, projectAddress,
					erfNo, totalFee, feePaid, deadline);
			

			// Create the Persons objects for architect, contractor, and customer respectively
			// for the architect:
			String architect = "architect";
			Person architectProject = new Person(architect, architectName, architectTelephone, 
					architectEmail, architectAddress);
			Person architectDummy = new Person(architect, "Loras", "0782741012", "Loras@gmail.com", "3 HighGarden road");

			// for the contractor:
			String contractor = "contractor";
			Person contractorProject = new Person(contractor, contractorName, contractorTelephone, 
					contractorEmail, contractorAddress);
			Person contractorDummy = new Person(contractor, "Jamie", "0781233455", "Jamie@gmail.com", "4 Castly Rock");
			
			// for the customer:
			String customer = "customer";
			Person customerProject = new Person(customer, customerName, customerTelephone, 
					customerEmail, customerAddress);
			Person customerDummy = new Person(customer, "Elena", "078123456", "Elena@gmail.com", "5 High Garden");
		}
		
		else if (menu == 2) {
			System.out.println();
			System.out.println("The current due date of this task is " + dummy.deadline);
			System.out.println(project.projectName);
			System.out.println("You would like to change the deadline of this task.");
			System.out.println("Please enter the new duedate: (dd/mm/yyyy):");
			String newDeadline = scanner.nextLine();
			Object project;
			project.deadline = newDeadline;
			
			
		}
	}

}
