public class Project {

	// Attributes
	int projectNo;
	String projectName;
	String buildingType;
	String projectAddress;
	String erfNo;
	double totalFee;
	double feePaid;
	String deadline;
	boolean isFinished = false;

	public Project(int projectNo, String projectName, String buildingType, String projectAddress,
			String erfNo, double totalFee, double feePaid, String deadline, boolean isFinished) {
		this.projectName = projectName;
		this.projectNo = projectNo;
		this.buildingType = buildingType;
		this.projectAddress = projectAddress;
		this.erfNo = erfNo;
		this.totalFee = totalFee;
		this.feePaid = feePaid;
		this.deadline = deadline;
	}

	public boolean isFinished() {
		return isFinished = true;
	}

	public String toString() {
		String output = "Project no: " + projectNo;
		output += "\nProject name: " + projectName;
		output += "\nBuilding type: " + buildingType;
		output += "\nProject Address: " + projectAddress;
		output += "\nERF number: " + erfNo;
		output += "\nProject cost: " + totalFee;

		return output;
	}
}