# RepoView-Insights
## Project Report: Extract Data using API

## Introduction
	The project involves the development of a Python script to fetch and visualize the view counts of public GitHub repositories associated with a specific user.
	It utilizes the GitHub API to collect repository data and the Matplotlib library for data visualization.

## Algorithm Explanation
	Library Imports
o	`requests` and `matplotlib.pyplot` libraries are imported for making API requests and data visualization, respectively.

	GitHub Credentials and Parameters
o	`username` and `token` are defined for GitHub authentication.
o	`base_url` is constructed to specify the endpoint for fetching the user's repositories.
o	A `query` is defined to filter public repositories.
o	`headers` and `params` dictionaries are created with necessary headers and query parameters for API requests.

	Function: `get_repository_views(repo_owner, repo_name)
o	A function to fetch view counts for a specified repository.
o	Endpoint for the GitHub traffic views API is constructed.
o	An HTTP GET request is made with appropriate headers, and the response is parsed as JSON.
o	If the request is successful (status code 200), the view count is extracted and returned. Otherwise, an error is reported.

	Data Collection
o	Lists for repository names and view counts are initialized.


	Retrieve Repository Data
o	An HTTP GET request is made to `base_url` with the provided headers and query parameters.
o	The response is checked for errors, and JSON data is parsed.
o	For each repository, the username, repository name, and view count are collected using the `get_repository_views` function if available.

	Data Visualization
o	A horizontal bar chart is created using Matplotlib.
o	Repository names are displayed on the y-axis, and view counts are plotted on the x-axis.
o	The chart is customized with a title, axis labels, and an inverted y-axis.
o	The chart is displayed using `plt.show()`.

## Conclusion
	The project successfully demonstrates how to utilize the GitHub API to retrieve and visualize view counts for public repositories owned by a specific GitHub user.
	This tool can be valuable for users who want to monitor and compare the popularity of their GitHub repositories.

## Future Enhancements
	Possible future enhancements include adding error handling for authentication, implementing pagination for users with more than 100 repositories, and providing options for different types of visualizations.


## References
	GitHub API Documentation: [https://docs.github.com/en/rest](https://docs.github.com/en/rest)
	Matplotlib Documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
