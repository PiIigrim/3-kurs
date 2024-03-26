using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormsApp1
{
    public partial class ManualPrint : Form
    {
        List<Group> tempGroups;
        public ManualPrint(List<Group> groups)
        {
            tempGroups = groups;
            InitializeComponent();
        }

        private void AddElButton_Click(object sender, EventArgs e)
        {
            if (GroupCount.Text == "" || GroupLeader.Text == "" || GroupName.Text == "") return;
            else
            {
                dataGridView1.Rows.Add(GroupName.Text, GroupLeader.Text, GroupCount.Text);
                tempGroups.Add(new Group(GroupName.Text, GroupLeader.Text, int.Parse(GroupCount.Text)));
            }
        }

        private void SaveTableButton_Click(object sender, EventArgs e)
        {
            Close();
        }

    }
}
