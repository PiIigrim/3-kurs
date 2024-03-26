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
    public partial class SearchRecordForm : Form
    {
        List<Group> groups;
        public SearchRecordForm(List<Group> Groups)
        {
            groups = Groups;
            InitializeComponent();
        }

        private void FoundButton_Click(object sender, EventArgs e)
        {
            IEnumerable<Group> IEG = groups;
            if (checkBox1.Checked) IEG = IEG.Where(e => e.GroupName == GroupName.Text);
            if (checkBox2.Checked) IEG = IEG.Where(e => e.GroupLeader == GroupLeader.Text);
            if (checkBox3.Checked) IEG = IEG.Where(e => e.StudentCount == int.Parse(GroupCount.Text));
            if (IEG.Count() == 0 || (!checkBox1.Checked&& !checkBox2.Checked && !checkBox3.Checked)) MessageBox.Show("Не было найдено никаких записей");
            else MessageBox.Show(IEG.ElementAt(0).GroupName + " , " + IEG.ElementAt(0).GroupLeader + " , " + IEG.ElementAt(0).StudentCount);
            Close();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}
