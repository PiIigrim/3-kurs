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
    public partial class NewDB : Form
    {
        RecordList RL;
        string? filepath;
        List<Group> groups = new List<Group>();
        public NewDB(RecordList recordList)
        {
            InitializeComponent();
            RL = recordList;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        //saveas
        private void button1_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.Cancel) return;
            filepath = saveFileDialog1.FileName;
            textBox2.Text = filepath;
            button2.Enabled = true;
            button3.Enabled = true;
        }
        //manprint
        private void button2_Click(object sender, EventArgs e)
        {
            ManualPrint Mp = new ManualPrint(groups);
            Mp.ShowDialog();
        }
        //create
        private void button3_Click(object sender, EventArgs e)
        {
            RL.SaveToFile();
            RL.SetGroups(groups);
            RL.SetPath(filepath);
            RL.SaveToFile();
            Close();
        }
    }
}
