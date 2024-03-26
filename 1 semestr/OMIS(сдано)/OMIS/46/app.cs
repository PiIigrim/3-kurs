using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace StudentGroupsApp
{
    // Класс, представляющий группу студентов
    public class Group
    {
        public string GroupName { get; set; }
        public string GroupLeader { get; set; }
        public int StudentCount { get; set; }
    }

    // Класс, представляющий список записей
    public class RecordList
    {
        private List<Group> groups;
        private string filePath;

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

        public List<Group> GetSortedRecords(string sortBy)
        {
            switch (sortBy)
            {
                case "groupName":
                    return groups.OrderBy(g => g.GroupName).ToList();
                case "groupLeader":
                    return groups.OrderBy(g => g.GroupLeader).ToList();
                case "studentCount":
                    return groups.OrderBy(g => g.StudentCount).ToList();
                default:
                    return groups;
            }
        }

        public Group FindFirstRecordByNumber(int number)
        {
            return groups.FirstOrDefault(g => g.StudentCount == number);
        }

        public Group FindFirstRecordByTemplate(string template)
        {
            return groups.FirstOrDefault(g => g.GroupName.Contains(template) || g.GroupLeader.Contains(template));
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
                    string line;
                    while ((line = reader.ReadLine()) != null)
                    {
                        string[] parts = line.Split(';');
                        if (parts.Length == 3)
                        {
                            Group group = new Group
                            {
                                GroupName = parts[0],
                                GroupLeader = parts[1],
                                StudentCount = int.Parse(parts[2])
                            };
                            groups.Add(group);
                        }
                    }
                }
            }
        }
    }

    // Главное окно приложения
    public class MainForm : Form
    {
        private RecordList recordList;
        private string fileName = "groups.txt"; // Имя файла для хранения записей
        private ListBox listBox;
        private Button addButton;
        private Button removeButton;

        public MainForm()
        {
            recordList = new RecordList(fileName);
            recordList.LoadFromFile();

            listBox = new ListBox();
            addButton = new Button { Text = "Добавить" };
            removeButton = new Button { Text = "Удалить" };

            addButton.Click += addButton_Click;
            removeButton.Click += removeButton_Click;

            Controls.Add(listBox);
            Controls.Add(addButton);
            Controls.Add(removeButton);

            UpdateList();
        }

        private void UpdateList()
        {
            listBox.Items.Clear();
            foreach (Group group in recordList.GetSortedRecords("groupName"))
            {
                listBox.Items.Add($"{group.GroupName} (Староста: {group.GroupLeader}, Студентов: {group.StudentCount})");
            }
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            using (var form = new AddRecordForm())
            {
                if (form.ShowDialog() == DialogResult.OK)
                {
                    recordList.AddRecord(form.Group);
                    recordList.SaveToFile();
                    UpdateList();
                }
            }
        }

        private void removeButton_Click(object sender, EventArgs e)
        {
            if (listBox.SelectedIndex >= 0)
            {
                int index = listBox.SelectedIndex;
                Group group = recordList.GetSortedRecords("groupName")[index];
                recordList.RemoveRecord(group);
                recordList.SaveToFile();
                UpdateList();
            }
        }
    }

    // Форма для добавления новой записи группы
    public class AddRecordForm : Form
    {
        private TextBox nameTextBox;
        private TextBox leaderTextBox;
        private TextBox countTextBox;
        private Button addButton;

        public Group Group { get; private set; }

        public AddRecordForm()
        {
            nameTextBox = new TextBox();
            leaderTextBox = new TextBox();
            countTextBox = new TextBox();
            addButton = new Button { Text = "Добавить" };

            Controls.Add(new Label { Text = "Название группы:", Top = 10 });
            Controls.Add(nameTextBox);
            Controls.Add(new Label { Text = "Староста:", Top = 40 });
            Controls.Add(leaderTextBox);
            Controls.Add(new Label { Text = "Численность студентов:", Top = 70 });
            Controls.Add(countTextBox);
            Controls.Add(addButton);

            addButton.Click += addButton_Click;
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            if (int.TryParse(countTextBox.Text, out int count))
            {
                Group = new Group
                {
                    GroupName = nameTextBox.Text,
                    GroupLeader = leaderTextBox.Text,
                    StudentCount = count
                };
                DialogResult = DialogResult.OK;
                Close();
            }
            else
            {
                MessageBox.Show("Некорректное значение для численности студентов.");
            }
        }
    }

    public static class Program
    {
        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}