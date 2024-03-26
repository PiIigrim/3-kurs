namespace WinFormsApp1
{
    partial class FillListForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            AddElementButton = new Button();
            GroupCount = new TextBox();
            GroupCountRO = new TextBox();
            GroupLeader = new TextBox();
            GroupLeaderRO = new TextBox();
            GroupName = new TextBox();
            GroupNameRO = new TextBox();
            SuspendLayout();
            // 
            // AddElementButton
            // 
            AddElementButton.Location = new Point(109, 318);
            AddElementButton.Name = "AddElementButton";
            AddElementButton.Size = new Size(145, 66);
            AddElementButton.TabIndex = 6;
            AddElementButton.Text = "Добавить";
            AddElementButton.UseVisualStyleBackColor = true;
            AddElementButton.Click += AddElementButton_Click;
            // 
            // GroupCount
            // 
            GroupCount.Location = new Point(198, 202);
            GroupCount.Name = "GroupCount";
            GroupCount.Size = new Size(150, 31);
            GroupCount.TabIndex = 12;
            // 
            // GroupCountRO
            // 
            GroupCountRO.Location = new Point(25, 202);
            GroupCountRO.Name = "GroupCountRO";
            GroupCountRO.ReadOnly = true;
            GroupCountRO.Size = new Size(150, 31);
            GroupCountRO.TabIndex = 11;
            GroupCountRO.Text = "Численность";
            // 
            // GroupLeader
            // 
            GroupLeader.Location = new Point(198, 115);
            GroupLeader.Name = "GroupLeader";
            GroupLeader.Size = new Size(150, 31);
            GroupLeader.TabIndex = 10;
            // 
            // GroupLeaderRO
            // 
            GroupLeaderRO.Location = new Point(25, 115);
            GroupLeaderRO.Name = "GroupLeaderRO";
            GroupLeaderRO.ReadOnly = true;
            GroupLeaderRO.Size = new Size(150, 31);
            GroupLeaderRO.TabIndex = 9;
            GroupLeaderRO.Text = "Староста";
            // 
            // GroupName
            // 
            GroupName.Location = new Point(198, 38);
            GroupName.Name = "GroupName";
            GroupName.Size = new Size(150, 31);
            GroupName.TabIndex = 8;
            // 
            // GroupNameRO
            // 
            GroupNameRO.Location = new Point(25, 38);
            GroupNameRO.Name = "GroupNameRO";
            GroupNameRO.ReadOnly = true;
            GroupNameRO.Size = new Size(150, 31);
            GroupNameRO.TabIndex = 7;
            GroupNameRO.Text = "Имя группы";
            // 
            // AddElem
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(369, 450);
            Controls.Add(GroupCount);
            Controls.Add(GroupCountRO);
            Controls.Add(GroupLeader);
            Controls.Add(GroupLeaderRO);
            Controls.Add(GroupName);
            Controls.Add(GroupNameRO);
            Controls.Add(AddElementButton);
            Name = "AddElem";
            Text = "AddElem";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private Button AddElementButton;
        private TextBox GroupCount;
        private TextBox GroupCountRO;
        private TextBox GroupLeader;
        private TextBox GroupLeaderRO;
        private TextBox GroupName;
        private TextBox GroupNameRO;
    }
}