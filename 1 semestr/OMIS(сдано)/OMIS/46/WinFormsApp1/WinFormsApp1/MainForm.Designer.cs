namespace WinFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            dataGridView1 = new DataGridView();
            NameGroup = new DataGridViewTextBoxColumn();
            HeaderGroup = new DataGridViewTextBoxColumn();
            Count = new DataGridViewTextBoxColumn();
            menuStrip1 = new MenuStrip();
            создатьСписокToolStripMenuItem = new ToolStripMenuItem();
            открытьсписокToolStripMenuItem = new ToolStripMenuItem();
            записьЗаЗаписьюToolStripMenuItem = new ToolStripMenuItem();
            поискПервойЗаписиToolStripMenuItem = new ToolStripMenuItem();
            добавитьСписокToolStripMenuItem = new ToolStripMenuItem();
            openFileDialog1 = new OpenFileDialog();
            textBox1 = new TextBox();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            menuStrip1.SuspendLayout();
            SuspendLayout();
            // 
            // dataGridView1
            // 
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            dataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.AllCells;
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Columns.AddRange(new DataGridViewColumn[] { NameGroup, HeaderGroup, Count });
            dataGridView1.Dock = DockStyle.Fill;
            dataGridView1.EditMode = DataGridViewEditMode.EditProgrammatically;
            dataGridView1.Location = new Point(0, 33);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.RowHeadersWidth = 62;
            dataGridView1.RowTemplate.Height = 33;
            dataGridView1.Size = new Size(890, 628);
            dataGridView1.TabIndex = 0;
            dataGridView1.CellContentClick += dataGridView1_CellContentClick;
            dataGridView1.UserDeletingRow += dataGridView1_UserDeletingRow;
            // 
            // NameGroup
            // 
            NameGroup.HeaderText = "Имя Группы";
            NameGroup.MinimumWidth = 8;
            NameGroup.Name = "NameGroup";
            // 
            // HeaderGroup
            // 
            HeaderGroup.HeaderText = "Староста";
            HeaderGroup.MinimumWidth = 8;
            HeaderGroup.Name = "HeaderGroup";
            // 
            // Count
            // 
            Count.HeaderText = "Численность";
            Count.MinimumWidth = 8;
            Count.Name = "Count";
            // 
            // menuStrip1
            // 
            menuStrip1.ImageScalingSize = new Size(24, 24);
            menuStrip1.Items.AddRange(new ToolStripItem[] { создатьСписокToolStripMenuItem, открытьсписокToolStripMenuItem, записьЗаЗаписьюToolStripMenuItem, поискПервойЗаписиToolStripMenuItem, добавитьСписокToolStripMenuItem });
            menuStrip1.Location = new Point(0, 0);
            menuStrip1.Name = "menuStrip1";
            menuStrip1.Size = new Size(890, 33);
            menuStrip1.TabIndex = 1;
            menuStrip1.Text = "menuStrip1";
            menuStrip1.ItemClicked += menuStrip1_ItemClicked;
            // 
            // создатьСписокToolStripMenuItem
            // 
            создатьСписокToolStripMenuItem.Name = "создатьСписокToolStripMenuItem";
            создатьСписокToolStripMenuItem.Size = new Size(154, 29);
            создатьСписокToolStripMenuItem.Text = "Создать список";
            создатьСписокToolStripMenuItem.Click += создатьСписокToolStripMenuItem_Click;
            // 
            // открытьсписокToolStripMenuItem
            // 
            открытьсписокToolStripMenuItem.Name = "открытьсписокToolStripMenuItem";
            открытьсписокToolStripMenuItem.Size = new Size(159, 29);
            открытьсписокToolStripMenuItem.Text = "Открыть список";
            открытьсписокToolStripMenuItem.Click += открытьсписокToolStripMenuItem_Click;
            // 
            // записьЗаЗаписьюToolStripMenuItem
            // 
            записьЗаЗаписьюToolStripMenuItem.Name = "записьЗаЗаписьюToolStripMenuItem";
            записьЗаЗаписьюToolStripMenuItem.Size = new Size(194, 29);
            записьЗаЗаписьюToolStripMenuItem.Text = "\"Запись за записью\"";
            записьЗаЗаписьюToolStripMenuItem.Click += записьЗаЗаписьюToolStripMenuItem_Click;
            // 
            // поискПервойЗаписиToolStripMenuItem
            // 
            поискПервойЗаписиToolStripMenuItem.Name = "поискПервойЗаписиToolStripMenuItem";
            поискПервойЗаписиToolStripMenuItem.Size = new Size(205, 29);
            поискПервойЗаписиToolStripMenuItem.Text = "Поиск первой записи";
            поискПервойЗаписиToolStripMenuItem.Click += поискПервойЗаписиToolStripMenuItem_Click;
            // 
            // добавитьСписокToolStripMenuItem
            // 
            добавитьСписокToolStripMenuItem.Name = "добавитьСписокToolStripMenuItem";
            добавитьСписокToolStripMenuItem.Size = new Size(165, 29);
            добавитьСписокToolStripMenuItem.Text = "Добавить запись";
            добавитьСписокToolStripMenuItem.Click += добавитьСписокToolStripMenuItem_Click;
            // 
            // openFileDialog1
            // 
            openFileDialog1.FileName = "openFileDialog1";
            openFileDialog1.Filter = "Текстовые файлы(*.txt)|*.txt";
            // 
            // textBox1
            // 
            textBox1.Location = new Point(0, 630);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(890, 31);
            textBox1.TabIndex = 2;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(890, 661);
            Controls.Add(textBox1);
            Controls.Add(dataGridView1);
            Controls.Add(menuStrip1);
            MainMenuStrip = menuStrip1;
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            FormClosing += Form1_FormClosing;
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            menuStrip1.ResumeLayout(false);
            menuStrip1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private DataGridView dataGridView1;
        private DataGridViewTextBoxColumn NameGroup;
        private DataGridViewTextBoxColumn HeaderGroup;
        private DataGridViewTextBoxColumn Count;
        private MenuStrip menuStrip1;
        private ToolStripMenuItem создатьСписокToolStripMenuItem;
        private ToolStripMenuItem записьЗаЗаписьюToolStripMenuItem;
        private ToolStripMenuItem поискПервойЗаписиToolStripMenuItem;
        private ToolStripMenuItem добавитьСписокToolStripMenuItem;
        private ToolStripMenuItem открытьсписокToolStripMenuItem;
        private OpenFileDialog openFileDialog1;
        private TextBox textBox1;
    }
}