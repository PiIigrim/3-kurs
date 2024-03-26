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
    public partial class OneToOne : Form
    {
        public List<Group> Groups;
        public int currentIndex;
        public OneToOne(List<Group> groups)
        {
            Groups = groups;
            currentIndex = 0;
            InitializeComponent();
            if (Groups.Count > 0) { ChangeAllText(); }
        }
        private void ChangeAllText()
        {

            IndexGroup.Text = (currentIndex + 1).ToString();
            GroupName.Text = Groups[currentIndex].GroupName;
            GroupLeader.Text = Groups[currentIndex].GroupLeader;
            GroupCount.Text = Groups[currentIndex].StudentCount.ToString();
        }
        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void ToRight_Click(object sender, EventArgs e)
        {
            if (currentIndex + 1 > Groups.Count - 1) return;
            else { ++currentIndex; ChangeAllText(); }
        }

        private void ToLeft_Click(object sender, EventArgs e)
        {
            if (currentIndex - 1 < 0) return;
            else { --currentIndex; ChangeAllText(); }
        }

        private void ToEndRight_Click(object sender, EventArgs e)
        {
            currentIndex = Groups.Count - 1; ChangeAllText();
        }

        private void ToEndLeft_Click(object sender, EventArgs e)
        {
            currentIndex = 0; ChangeAllText();
        }

        private void OneToOne_Load(object sender, EventArgs e)
        {

        }
    }
}
