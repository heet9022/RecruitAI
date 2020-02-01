-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 01, 2020 at 06:41 PM
-- Server version: 10.1.39-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recruitai`
--

-- --------------------------------------------------------

--
-- Table structure for table `profiles`
--

CREATE TABLE `profiles` (
  `idd` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `skills` varchar(500) NOT NULL,
  `exp` varchar(10000) NOT NULL,
  `about` varchar(10000) NOT NULL,
  `title` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles`
--

INSERT INTO `profiles` (`idd`, `name`, `location`, `skills`, `exp`, `about`, `title`) VALUES
(5, 'Gaurav Dhiman', 'Chandigarh, Chandigarh, India', '', 'Sr. Python DeveloperCompany NameImpinge SolutionsDates EmployedJan 2018 – PresentEmployment Duration2 yrs 2 mosLocationMohali, Punjab, IndiaLaguage: Python, React,  Nodejs, UI(HTML, CSS, JS etc)Database: MongoDB, PostgreSQL, MySQL, SqliteFramework: Django, Flask, EVE, django-rest-framework, flask-rest-frameworkVersion Control: GitHub, BitbucketCloud Platform: AWS(EC2, S3, Bucket, etc) , Heroku, Mlab(for mongo)OS: Linux (modification baserc file and some functionality )My blogs-http://easywaytostudy.herokuapp.com/post/XBOQIGWMNT2Zhttp://python-blogs.herokuapp.com…Python DeveloperCompany NameWeavebytes Infotech Pvt. Ltd. - IndiaDates EmployedApr 2017 – Jan 2018Employment Duration10 mosLocationMohali, Punjab, IndiaDjango / Flask / Machine Learning / Blockchain / Internet of Things (IoT)  / + MoreJava Software DeveloperCompany NamePC Technology Pvt. Ltd.Dates EmployedSep 2015 – Mar 2017Employment Duration1 yr 7 mosLocationDehra Dun Area, India* Creating Window based application using swing (GUI widget toolkit) AWT.* Creating Front-End applications using JSP(JavaServer Pages) amd Servlet.* Database: Using ORACLE* Framework: Spring, Structs and Hibernate.', 'I\'m a multi-skilled Python (Django, Flask,  Webapp2) professional with rich experience in building real-time complex webprojects, API development using Node JS (MEAN Stack) and Python(Django rest framework & Flask rest framework),Databases like Mongo DB, PostgreSQL, Sqlite, Mysql along with Redis, Socket.io, Server Management(AWS, L...\n            see more', 'Sr. Python Developer at Impinge Solutions (8218867658, 8899737453)'),
(6, 'Parth Modi', 'Ahmedabad, Gujarat, India', '\n          HTML\n        \n            JavaScript\n          \n          Cascading Style Sheets (CSS)\n        ', 'Company NameNiviData TechnologyTotal Duration2 yrs 9 mosTitlePython-Django DeveloperDates EmployedJun 2017 – PresentEmployment Duration2 yrs 9 mosLocationAhmedabad Area, IndiaTitlePython DeveloperFull-timeDates EmployedJun 2017 – PresentEmployment Duration2 yrs 9 mosLocationAhmedabadTitlePython-Django DeveloperDates EmployedJun 2017 – PresentEmployment Duration2 yrs 9 mosLocationAhmedabad Area, IndiaTitlePython DeveloperFull-timeDates EmployedJun 2017 – PresentEmployment Duration2 yrs 9 mosLocationAhmedabad', 'To Summarise my work experience I can say that to work with django and python is really fun. Each and every day I usedto learn something new. Sometimes it takes time to understand but at the end implementation of the new module feelswonderful. In my job I have worked with many libraries which I mentioned in my profile but still I want to wor...\n            see more', 'Python Developer'),
(7, 'Shashank Verma', 'Gurgaon, Haryana, India', '\n          Python\n        \n          Django\n        \n          Flask\n        ', 'Python DeveloperCompany NameKellton Tech Solutions LimitedDates EmployedDec 2018 – PresentEmployment Duration1 yr 3 mosLocationGurgaon, IndiaPython DeveloperCompany NameAppinventivDates EmployedMay 2018 – Nov 2018Employment Duration7 mosLocationNoida Area, IndiaPython DeveloperCompany NameCoding Cart TechnologiesDates EmployedNov 2016 – Apr 2018Employment Duration1 yr 6 mosLocationChandigarh Area, IndiaPython/Django DeveloperCompany NameEsteem Finventures LimitedDates EmployedMar 2016 – Sep 2016Employment Duration7 mosWorked with highly professional team members,understand full flow of project development. Developed REST API and JSON response using Python(2.7) and Dajngo(1.9.7). Covered deep knowledge of MVT(model,view,template) framework and PostgreSQL database server. Understood deployment of project on server. Used MantisBT for bug reporting ,SVN as sub versioning tool and Pycharm Community Edition IDE on CentOS operating system.…', 'Total 3+ year of professional experience in web development on Python, Django and Flask.Worked on both Python 2.7 and 3.x.Hands-on experience in developing web applications from scratch....\n            see more', 'Python Developer'),
(8, 'Bharat Bhushan', 'Bhopal, Madhya Pradesh, India', '\n            Python\n          \n            Django\n          \n            Google Cloud Platform\n          ', 'Python DeveloperCompany NameNickelfoxDates EmployedNov 2018 – PresentEmployment Duration1 yr 4 mosLocationNoida Area, IndiaPython DeveloperCompany NameLinkites Infotech Pvt LtdDates EmployedNov 2017 – Oct 2018Employment Duration1 yrLocationIndore, Madhya Pradesh, IndiaPHP And Python DeveloperCompany NameCanopus Infosystems Pvt. Ltd. (ISO 9001:2008)Dates EmployedJul 2016 – Oct 2017Employment Duration1 yr 4 mosLocationIndore Area, India', 'Experienced PHP And Python Developer with a demonstrated history of working in the Software Development industry.Skilled in mySQL, PHP development, Python Development, Google Cloud Platform, Google App Engine. Strongengineering professional with a Bachelor\'s degree focused in Information Technology from Radharaman insti...\n            see more', 'Python Developer at Nickelfox'),
(9, 'Nil Patel', 'Navsari, Gujarat, India', '\n            Python\n          \n            Django\n          \n          ElasticSearch\n        ', '', 'Experienced Python Developer with a demonstrated history of working in the information technology and servicesindustry. Skilled in J2EE Web Services, Python (Programming Language), Hibernate, Servlets, and Spring Framework.Strong engineering professional with a Bachelor of Engineering - BE focused in Computer Engineering from P...\n            see more', 'Python Developer at Appscrip'),
(10, 'Sugesh Vandli', 'Bengaluru, Karnataka, India', '\n            Python\n          \n            Django\n          \n            MySQL\n          ', 'Python DeveloperCompany NameJPMorgan Chase & Co.Dates EmployedJan 2017 – PresentEmployment Duration3 yrs 2 mosLocationBengaluru Area, IndiaPython DeveloperCompany NameNokia NetworksDates EmployedFeb 2015 – Dec 2016Employment Duration1 yr 11 mosLocationBengaluru, Karnataka, IndiaSoftware EngineerCompany NameLG Soft IndiaDates EmployedJul 2012 – Jan 2015Employment Duration2 yrs 7 mos', 'I am a Python Developer with 7+ years of experience in the industry. I have experience in Finance Technology domainand I haveBackend development experience with Python....\n            see more', 'Python Developer at JPMorgan Chase & Co.'),
(11, 'Vishal Ghuge', 'Pune, Maharashtra, India', '\n            Python\n          \n            Machine Learning\n          \n            Pandas\n          ', 'Python DeveloperCompany NamefreelancerFull-timeDates EmployedMar 2019 – PresentEmployment Duration1 yrLocationPune Area, IndiaPython developerCompany NameNividous software solutionFull-timeDates EmployedJan 2018 – Mar 2019Employment Duration1 yr 3 mosLocationMumbai, Maharashtra, IndiaWorked as a product development engineerPython DeveloperCompany NamePrognosticsoft Solutions Pvt LtdDates EmployedJun 2016 – Dec 2017Employment Duration1 yr 7 mosLocationPune, Maharashtra, India', 'Python Developer with a demonstrated history of working in the computer software industry. Skilled in Python(Programming Language), SQL, Data Science, Data Analytics, PySpark, Hive, MySQL, Flask, Pandas (Software), ApacheAirflow, Flask, Django, IBM Watson, Microsoft Azure and HTML. Strong engineering professional with a BCA f...\n            see more', 'Python Developer'),
(12, 'Jaysheel U.', 'Pune, Maharashtra, India', '\n            Python\n          \n            Django\n          \n            SQL\n          ', 'Python DeveloperCompany NameBackpacker PandaDates EmployedJan 2018 – PresentEmployment Duration2 yrs 2 mosLocationPune, Maharashtra, IndiaDjango DeveloperCompany NamePracTutorDates EmployedApr 2017 – Aug 2017Employment Duration5 mosLocationAhmedabad Area, IndiaSoftware EngineerCompany NameSelf-employedDates EmployedNov 2016 – Apr 2017Employment Duration6 mosLocationAhmedabad Area, IndiaJr. Software EngineerCompany NameQuixom TechnologyDates EmployedJul 2015 – Dec 2016Employment Duration1 yr 6 mosDeveloping Kodi Addons and skin. And communicate with client for daily updates and enhancements in the app I am working on.Skin DeveloperCompany NameCovert MediaDates Employed2016Employment Durationless than a yearDeveloping the skin for Covert Media and making sure their required design is achieved as a Freelancer', 'Developing web based application and know languages such as Java , Python and C++. I have strong command andpractice in python.... see more', 'Python Developer at Backpacker Panda'),
(13, 'Saraswathi K', 'India', '', '', '4 years of experience in Python and Java Development.Good Knowledge and Experience in Core Python, Data Analysis Using Python(Quartz), Network Automation usingPython, Good knowledge on Object Oriented Concepts and Data Structures of Python. Hands on Experience ...\n            see more', 'Software Engineer at Tata Consultancy Services'),
(14, 'Rakesh Chopkar [Python Developer]', 'Pune, Maharashtra, India', '\n            Python\n          \n            XML\n          \n            Selenium\n          ', 'Senior Software EngineerCompany NameDell EMCDates EmployedSep 2017 – PresentEmployment Duration2 yrs 6 mosLocationPune Area, IndiaSenior Software EngineerCompany NameCapgeminiDates EmployedDec 2014 – Sep 2017Employment Duration2 yrs 10 mosLocationPuneJunior Software EngineerCompany NameEmtec Inc.Dates EmployedAug 2013 – Dec 2014Employment Duration1 yr 5 mosLocationpuneJunior software engineerPython developerCompany NamePropylon infotech services puneDates EmployedApr 2012 – Aug 2013Employment Duration1 yr 5 mos', 'Experienced Senior Software Engineer with a demonstrated history of working in the information technology andservices industry. Skilled in vCenter Server, Python (Programming Language), VMware NSX, Linux, and Storage. Strongengineering professional with a Bachelor of Engineering (BE) focused in Information Technology from Baba sa...\n            see more', 'Senior Software Engineer in DellEmc Pune:\nPython, Storage, VMware.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `profiles`
--
ALTER TABLE `profiles`
  ADD PRIMARY KEY (`idd`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `profiles`
--
ALTER TABLE `profiles`
  MODIFY `idd` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
