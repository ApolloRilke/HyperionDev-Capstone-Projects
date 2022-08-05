import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Poised {

	public static void main(String[] args) {

		// Initialise scanner
		Scanner scanner = new Scanner(System.in);

		// Display an introduction message and what user will be doing.
		System.out.println("This is the Poised Project Management System.");
		System.out.println("Please enter the details of the project:");

		// USer enters the project details
		System.out.println("What is the project title?");
		String projectName = scanner.nextLine();

		// Enter the project number
		System.out.println("What is the project number?");	
		int projectNo = scanner.nextInt();
		scanner.nextLine();

		// Enter the building type
		System.out.println("What is the building type?");
		String buildingType = scanner.nextLine();

		// Enter the building address
		System.out.println("What is the building address?");
		String projectAddress = scanner.nextLine();

		// Enter the ERF number
		System.out.println("What is the project ERF number?");
		String erfNo = scanner.nextLine();

		// Enter the total cost of the project
		System.out.print("The total cost of the project? \nR");  	
		double totalFee = scanner.nextDouble();

		// Enter the amount of money that has been paid (could be 0, could be full amount)
		System.out.print("How much has already been paid to date? \nR");  	
		double feePaid = scanner.nextDouble();
		scanner.nextLine();

		// Enter the deadline for this project
		System.out.println("Enter the deadline: (dd/mm/yyyy)"); 
		// At this point, assume user enters correct date.
		String deadline = scanner.nextLine();
		System.out.println();

		// Project details relating to the persons involved.
		// The architect contact details to create Person object
		System.out.println("The following information will pertain to the architect assigned"
				+ " to this project.");
		System.out.println("Enter the name of the architect:");
		String architectName = scanner.nextLine(); 
		System.out.println("Enter their telephone number:");
		String architectTelephone = scanner.nextLine(); 
		System.out.println("Enter their email address:");
		String architectEmail = scanner.nextLine(); 
		System.out.println("Enter the relevant address:");
		String architectAddress = scanner.nextLine(); 
		System.out.println();

		// Contractor contact details to create Person object
		System.out.println("The following information will pertain to the contractor assigned"
				+ " to this project.");
		System.out.println("Enter the name of the contractor:");
		String contractorName = scanner.nextLine(); 
		System.out.println("Enter their telephone number:");
		String contractorTelephone = scanner.nextLine(); 
		System.out.println("Enter their email address:");
		String contractorEmail = scanner.nextLine(); 
		System.out.println("Enter the relvant address:");
		String contractorAddress = scanner.nextLine(); 
		System.out.println();

		// Customer contact details to create Person object
		System.out.println("The following information will pertain to the customer assigned"
				+ " to this project.");
		System.out.println("Enter the name of the customer:");
		String customerName = scanner.nextLine(); 
		System.out.println("Enter their telephone number:");
		String customerTelephone = scanner.nextLine(); 
		System.out.println("Enter their email address:");
		String customerEmail = scanner.nextLine(); 
		System.out.println("Enter the relevant address:");
		String customerAddress = scanner.nextLine(); 

		// If the project name is not entered, the default project name must be
		// the building type + last name of the architect assigned.
		if (projectName.isEmpty()) {
			// Split the architect name up by space " "
			String[] lastNameList = architectName.split(" ");
			// Isolate the last name of the architect
			String lastName = lastNameList[lastNameList.length -1];
			// Finalise the project name
			projectName = buildingType + " " + lastName;
		}

		// Create a Project Object from the user inputs
		Project project = new Project(projectNo, projectName, buildingType, projectAddress,
				erfNo, totalFee, feePaid, deadline, false);

		// Create the Persons objects for architect, contractor, and customer respectively
		// for the architect:
		String architect = "Architect";
		@SuppressWarnings("unused") // to suppress warnings for unused data as project is not yet
		// completed
		Person architectProject = new Person(architect, architectName, architectTelephone, 
				architectEmail, architectAddress);

		// for the contractor:
		String contractor = "Contractor";
		Person contractorProject = new Person(contractor, contractorName, contractorTelephone, 
				contractorEmail, contractorAddress);

		// for the customer:
		String customer = "Customer";
		Person customerProject = new Person(customer, customerName, customerTelephone, 
				customerEmail, customerAddress);
		System.out.println();

		// Display confirmation message that Project and Persons objects have been added
		System.out.println("You have successfully added the project " + projectName);
		System.out.println();


		// ALLOW USER TO CHANGE THE DEADLINE SECTION
		System.out.println("\nThe current due date of this task is " + project.deadline);
		System.out.println("You would like to change the deadline of this task?");
		System.out.println("y - yes \nn - no");  //"n" could also be anything else at the moment
		String changeDeadline = scanner.nextLine();

		// Change the deadline in the Project object to the new user input deadline    
		if (changeDeadline == "y") {
			System.out.println("Please enter the new duedate: (dd/mm/yyyy):");
			String newDeadline = scanner.nextLine();
			project.deadline = newDeadline;
		}


		// Change the total amount of the fee paid to date
		System.out.println("\nThe current amount paid on this project is R" + project.feePaid);
		System.out.println("Would you like to update this balance?");
		System.out.println("y - yes \nn - no");  //"n" could also be anything else at the moment
		String changeFeePaid = scanner.nextLine();

		if (changeFeePaid == "y") {
			System.out.println("Please add enter the updated balance /nR");
			int feePaidUpdate = scanner.nextInt();
			project.feePaid = feePaidUpdate;
		}

		// CHANGE THE CONTRACTOR CONTACT DETAIL SECTIOM
		// Change contractor's contact details. The user will see the specific contact detail,
		// ie email address, and hit enter if no update ie scanner is empty. If the user
		// inputs data, then this new data will replace the old data.

		// Display rules to user on how to change/update the contractor contact details
		System.out.println("The contact information for " + contractorProject.name + " will be");
		System.out.print(" displayed. \nPress enter to continue, or input new information.");

		// The user will see the telephone number on system, they update a new number or hit enter
		System.out.println(contractorProject.name + "'s telephone number: " 
				+ contractorProject.telephoneNo);
		String newContractorTelephone = scanner.nextLine();
		if (newContractorTelephone.isEmpty()) {
			contractorProject.telephoneNo = newContractorTelephone;
		}
		// The user will see the email address on system, they can input an update or hit enter
		System.out.println(contractorProject.name + "'s email: " + contractorProject.email);
		String newContractorEmail = scanner.nextLine();
		if (newContractorEmail.isEmpty()) {
			contractorProject.email = newContractorEmail;
		}
		// The user will see the address on system, then they can input an update or hit enter
		System.out.println(contractorProject.name + "'s address: " + contractorProject.address);
		String newContractorAddress = scanner.nextLine();
		if (newContractorAddress.isEmpty()) {
			contractorProject.address = newContractorEmail;
		}


		// FINALISATION SECTION
		System.out.println("This is the project finalisation section.");
		double amountOwed = project.totalFee - project.feePaid;

		// If the amount owed is positive, the invoice is displayed
		if (amountOwed > 0) {
			System.out.println("Here is the invoice:");
			System.out.println("The customers information:");
			System.out.println("Customer name: \t" + customerProject.name);
			System.out.println("Customer contact number: " + customerProject.telephoneNo);
			System.out.println("Customer email\t: " + customerProject.email);
			System.out.println("Customer address\t: " + customerProject.address);

			System.out.println();
			String formatedCurrency = String.format("%,.2f\"", amountOwed);
			System.out.println("The amount still to be paid is: R" + formatedCurrency);
		}
		// Else the project will continue to be marked as completed.
		else {
			// Mark the project as finished
			project.isFinished();
			if (project.isFinished) {
				//Insert information to text file

				// Completed date will use the date of assigning the project complete
				DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy");
				LocalDate localDate = LocalDate.now();
				String completedToday = dtf.format(localDate);
				System.out.println("This project has been completed on " + completedToday);
				
				// The toString for the Project and the Persons objects will be added to the text file.
			}
		}   
		scanner.close(); // close scanner
	} 
}