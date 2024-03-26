using System.Security.Cryptography.X509Certificates;

namespace WinFormsApp1
{
    //  ласс, представл€ющий группу студентов
    public class Group
    {
        public string? GroupName { get; set; }
        public string? GroupLeader { get; set; }
        public int StudentCount { get; set; }

        public Group(string GroupName,string GroupLeader,int StudentCount)
        {
            this.GroupName = GroupName;
            this.GroupLeader = GroupLeader;
            this.StudentCount = StudentCount;
        }
    }

    //  ласс, представл€ющий список записей
    public class RecordList
    {
        private List<Group> groups;
        private string filePath;

        public void SetPath(string filePath){
            this.filePath = filePath;
        }
        public string GetFilePath() { return filePath; }
        public void SetGroups(List<Group> groups) { this.groups = groups; }
        public List<Group> GetGroups() { return groups; }
        public RecordList(string fileName)
        {
            groups = new List<Group>();
            filePath = fileName;
        }
        public void AddRecord(Group group)
        {
            groups.Add(group);
        }
        public void RemoveRecord(Group group)
        {
            groups.Remove(group);
        }
        public void SaveToFile()
        {
            using (StreamWriter writer = new StreamWriter(filePath))
            {
                foreach (Group group in groups)
                {
                    string record = $"{group.GroupName};{group.GroupLeader};{group.StudentCount}";
                    writer.WriteLine(record);
                }
            }
        }
        public void LoadFromFile()
        {
            if (File.Exists(filePath))
            {
                using (StreamReader reader = new StreamReader(filePath))
                {
                    string? line;
                    while ((line = reader.ReadLine()) != null)
                    {
                        string[] parts = line.Split(';');
                        if (parts.Length == 3)
                        {
                            Group group = new Group(parts[0],parts[1],int.Parse(parts[2]));
                            groups.Add(group);
                        }
                    }
                }
            }
        }
    }
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            MainForm MainForm = new MainForm("C:\\Users\\Danik\\source\\repos\\WinFormsApp1\\TestDB.txt");
            MainForm.RewriteDB();
            Application.Run(MainForm);
        }
    }
}